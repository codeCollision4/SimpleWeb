# SimpleWeb
Simple web client and server

This project contatins three files of importance.

1. text500.txt is a test file that the server will send to clients as a string on request

2. simple_client is the client program that can send requests and received responses from localhost servers as well as ones over the internet

3. simple_server is the server program, once it is running it can receive requests and send responses to clients. It contains only one file that can be accessed. It can handle GET and HEAD requests. All others will receive a Not Implemented response header.

To use the client:

Make sure you are in the project directory before using the commands below

$ python simple_client.py

This will bring up the menu that will tell you to provide the method, host and pathname. Provide those by using the keyboard to input.

Ex
Enter method, host, and then pathname for connection. STOP as method to end client.
GET localhost text500.txt

This will output the response from the server and any data received.

To use the client and server:

First start the client using the below command. Make sure you are in a separate terminal window to do this. Ensure you are in the project directory.

$ python simple_server.py

This will output 

SERVER IS LISTENING

Now you can use the client to connect with the below commands

$python simple_client.py
Enter method, host, and then pathname for connection. STOP as method to end client.
GET localhost text500.txt

This will attempt to connect to the local server and retrieve the data from the file requested. The server will also have an output that presents helpful info on if the file was found, what's in the file and the header received from the client as well as what is sent to the client as a response. 

Thanks for reading!