PROJECT: CS361 Microservice A- check_type()<br/>
AUTHOR: Gilbert Keithline

IMPORTS<br/>
socket<br/>
pickle<br/>

# About
check_type() is a microservice that receives a list of dictionaries containing, as keys, the strings 'inputType' and 'inputValue'. The value for 'inputType' is a 
string describing a python object type ("string", "integer", etc) and the value for 'inputValue' is simply a python object. check_type() then verfies 
whether or not the 'inputValue' object type matches the one described in 'inputType' for each dictionary in the list. check_type() returns a dictionary containg a 
boolean with an error description and occurrences of mismatched type/values are logged to a .txt file.<br/>
Incorrectly formatted parameter lists return an error.

check_type() only supports types() int, str, and bool at this time.

# Instructions
To use check_type():<br/>
-open checkType_server.py in its own terminal as a background program<br/>
-place checkType_client.py in the directory of the project the user wishes to call it in<br/>
-from checkType_client import check_type
-the check_type() client closes automatically after each useage. To close the server, incorporate the command check_type('close') into the parent program closure sequence

## Request Data
To request data, simply call check_type(data) where 'data' is a correctly formatted list as described in the About section.

## Receive Data
data is automically received and returned by the check_type() function. No user action after the funciton call is necessary to receive data.

## UML Diagram
![Screenshot 2024-05-19 152542](https://github.com/GAKeithline/CS361_microserviceA_checkType/assets/137833914/8728ce9a-33af-47a2-bb16-71ff626744a0)



## Example
Here are some examples of correctly formatted check_type() calls and their returns:

data = [{'inputType': 'string', 'inputValue': 'string cheese'}, {'inputType': 'integer', 'inputValue': 6}, {'inputType': 'boolean', 'inputValue': True}]<br/>
'> check_type(data)' would return {'validated': True, 'error': None}

data = [{'inputType': 'string', 'inputValue': 14}, {'inputType': 'integer', 'inputValue': 6}]<br/>
'> check_type(data)' would return {'validated': False, 'error': '14 is not type: string'}

Here is an incorrectly formatted check_type() call and its return:

data = [{'inputType': 'string', 'inputValue': True, 'Third Key': 'Shouldn't be here'}]<br/>
'> check_type(data)' would return "Error: Please ensure your input is correctly formatted."
