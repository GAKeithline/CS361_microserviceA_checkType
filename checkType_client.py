import socket
import pickle


def check_type(data):
    """
    receives a list of dictionaries and communicates them to a server-side type validation program.
    Closes server if given parameter 'close'
    """

    # set up server and socket
    server_ip = "127.0.0.1"
    server_port = 8000
    client = socket.socket()
    client.connect((server_ip, server_port))

    try:
        # if close command is given, forward to server
        if type(data) is str and data.lower() == 'close':
            close_command = pickle.dumps(data.lower())
            client.send(close_command)
        # send data to server for type validation
        else:
            data_package = pickle.dumps(data)
            client.send(data_package)
            # receive results of validation and return to user
            response = pickle.loads(client.recv(1024))
            return response
    except Exception as error:
        print(f'Error: {error}')

        # client is built as a callable function and operates on an as-called basis
    finally:
        client.close()
