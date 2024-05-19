import socket
import pickle


class InvalidFormat(Exception):
    """a custom exception to be used with check_type() for when data is incorrectly templated"""
    pass

def check_type(data):
    """
    receives a list of dictionaries each containing two keys "inputType and inputValue". inputType refers to a string
    describing an object type ('string', 'integer', 'boolean') and inputValue refers to an object of any type.
    check_type() verifies that the type of inputValue matches that described in inputType and returns True if so.
    If there is a mismatch, an error message is returned instead. If parameter data is not in correct format,
    an exception is raised. Only supports str, int, and bool types.
    """

    try:
        # verify that the data is a list and not empty
        if type(data) is not list or len(data) < 1:
            raise Exception
        for index in data:
            # verify that the list items contain only 2 keys: type and value
            if 'inputType' not in index or 'inputValue' not in index or len(index) != 2:
                raise Exception
            # Check to see if inputValue types match the described types in inputType.
            if (index['inputType'] == 'string' and type(index['inputValue']) is str or
                    index['inputType'] == 'integer' and type(index['inputValue']) is int or
                    index['inputType'] == 'boolean' and type(index['inputValue']) is bool):
                pass
            # If there is a mismatch, or an object of an unsupported type, return an error message
            else:
                input_val = index['inputValue']
                input_type = index['inputType']
                return str(input_val) + " is not type: " + str(input_type)
        return True
    # if data parameter is not correctly formatted, raise exception.
    except:
        raise InvalidFormat


def run_server():
    """
    runs a continually listening server that receives data and runs the check_type() command on it. If check_type()
    returns True, the server returns a confirmation message to the client. If check_type() indicates a mismatch, the
    server returns a failure message to the client and logs the mismatch in a .txt file. If check_type() raises an
    exception, the server returns a 'check format' message to the client. Upon receiving the message 'close' the server
    closes.
    """
    # Establish server and listening socket
    server_ip = "127.0.0.1"
    port = 8000
    server = socket.socket()
    server.bind((server_ip, port))

    server.listen(0)
    print(f'listening on {server_ip}:{port}')

    while True: # server will listen until told not to.

        # receive data from socket
        client_socket, client_address = server.accept()
        print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
        request = pickle.loads(client_socket.recv(1024))

        # terminate socket loop if close command is received
        if request == 'close':
            break

        # Data type-validation
        else:
            try:
                data = check_type(request)
                if data is True:
                    results = {'validated': True, 'error': None}
                    print('type validation: pass')
                # return mismatches to client and log mismatch to .txt file
                else:
                    results = {'validated': False, 'error': data}
                    print('type validation: fail \n Mismatch logged in "mismatch.txt".')
                    with open('mismatch.txt', 'a') as outfile:
                        outfile.write('validated: False, ' + 'error: ' + data + '\n')
                # send results to client
                data_validation = pickle.dumps(results)
                client_socket.send(data_validation)

            # inform client of incorrectly formatted data
            except Exception as error:
                error_msg = (f'Error: Please ensure your input is correctly formatted.')
                print(error_msg)
                val_fail = pickle.dumps(error_msg)
                client_socket.send(val_fail)

    # close socket
    client_socket.close()
    print('Connection to client closed')
    server.close()


run_server()
