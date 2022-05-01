
import socket
import re

# Starup menu
method = ""
host = ""
pathname = ""
serverport = 0

while True:
    user_input = input("Enter method, host, and then pathname for connection. STOP as method to end client.\n")
    
    # Parsing user input: Method, host, pathname
    parse = user_input.split()
    method = parse[0]
    if method == 'STOP':
        exit(0) # End program if stop
    host = parse[1]
    pathname = parse[2]
    if host != "localhost": # Setting ports based on what host
        serverport = 80
    else:
        serverport = 60000

    # Establishing client socket 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, serverport)) # Connecting socket to host and port
        request = f"{method} /{pathname} HTTP/1.1\r\nHost: {host}\r\n\r\n" # Creating request string
        s.sendall(request.encode()) # Sending request as bytes
        response = s.recv(4096) # Getting first packet
        if method == "GET" and host != 'localhost': # Only using content length if Get req and not a localhost
            temp = response.decode() # Holding header to check content length
            # Check for Content Length
            m = re.search('Content-Length: \d+', temp)
            msg_len = int(m.group().split()[1])
            while len(response) < msg_len:
                packet = s.recv(4096) # Getting next and looping
                response = response + packet
        data = response.decode()

    # New line between user input and output
    print()

    # Printing Output
    print("CONNECTED TO SERVER")
    print("REQUEST MSG:\n" + request)

    # Parsing data
    idx = data.find("\r\n\r\n",0)
    header = data[:idx]
    body = data[idx:]

    # Outputting Response header
    print("RESPONSE HEADER FROM SERVER:")
    print(header)
    print("END OF HEADER\n\n")

    # Outputting body of html
    print("DATA RECEIVED:")
    if method == "HEAD":
        print("HEAD request, no data sent.")
    else:
        print(body)
    print("END OF DATA\n\n")
