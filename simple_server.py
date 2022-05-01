import socket
import os.path

host = "localhost"  # local host 127.0.0.1
serverport = 60000  # Port to listen on
response_dict = {"Get found": "HTTP/1.1 200 OK\r\n\r\n",
                 "Get not": "HTTP/1.1 404 Not Found\r\n\r\n",
                 "Head found": "HTTP/1.1 200 OK\r\n\r\n",
                 "Head not": "HTTP/1.1 404 Not Found\r\n\r\n",
                 "Not": "HTTP/1.1 501 Not Implemented\r\n\r\n"
                }
# Opens and closes socket 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, serverport)) #Binding welcoming socket
    s.listen(1) # Telling socket to listen
    print("SERVER IS LISTENING\n\n")
    while True:
        connectionSocket, addr = s.accept() # Accepting connection from client
        # Creating socket between server and client
        with connectionSocket:
            print(f"SERVER CONNECTED WITH {addr[0]}:{addr[1]}\n")
            request = connectionSocket.recv(4096) # getting request from client
            req_str = request.decode()
            # Client message
            print("MESSAGE RECEIVED FROM CLIENT:")
            print(req_str[:-3])
            print("END OF MESSAGE RECEIVED FROM CLIENT\n\n")

            # Parse message header
            print("[PARSE MESSAGE HEADER]:")
            req_comp = req_str.split()
            method = req_comp[0]
            dest = req_comp[1][1:]
            ver = req_comp[2]
            print(f"METHOD = {method}, DESTADDRESS = {dest}, HTTPVersion = {ver}\n\n")

            # Finding dest file and reading if found
            if method == "GET" or method == "HEAD":
                response = ""
                if os.path.exists(dest):
                    found = "FILE FOUND"
                    with open(dest, 'r') as f:
                        for line in f:
                            response = response + line
                    print(f"[LOOK UP]: {found}")
                    print("DATA SENT:")
                    print(response)
                    print("END OF DATA SENT\n\n")
                else:
                    found = "FILE NOT FOUND"
                    print(f"[LOOK UP]: {found}\n\n")
            else:
                print("UNKNOWN METHOD\n")

            
            # Sending response header
            print("RESPONSE HEADER TO CLIENT:")
            res_msg = ""
            res_header = ""
            # if cases for each header, trim newlines and print. Then send cat of header and data
            if method == "GET" and found == "FILE FOUND":
                res_msg = response_dict["Get found"] + response
                res_header = response_dict["Get found"][:-4]
            elif method == "GET" and found == "FILE NOT FOUND":
                res_msg = response_dict["Get not"] + response
                res_header = response_dict["Get not"][:-4]
            elif method == "HEAD" and found == "FILE FOUND":
                res_msg = response_dict["Head found"] + response
                res_header = response_dict["Head found"][:-4]
            elif method == "HEAD" and found == "FILE NOT FOUND":
                res_msg = response_dict["Head not"] + response
                res_header = response_dict["Head not"][:-4]
            else:
                res_msg = response_dict["Not"]
                res_header = response_dict["Not"]

            print(res_header)
            print("END OF HEADER TO CLIENT")

            # Sending data
            connectionSocket.sendall(res_msg.encode())
            

            