# sockets_in_python
using sockets module to interact with client and server

The module we use in python to deal with sockets is the socket module. Import socket and set
the HOST and PORT that our socket will be listening to, HOST = '127.0.0.1' OR localhost on our
local computer and the PORT = 65000 (non-privileged port), which means our socket will take
incoming connection from the address 127.0.0.1:65000

We will create a socket object using socket.socket() and socket type as socket.SOCK_STREAM

socket.socket() can create a context manager object which establishes a runtime object when 
executing a with statement. There is no need to call s.close()

The arguments passed to socket specify the internet address, socket.AF_INET is internet address
family for IPV4, socket.SOCK_STREAM is internet address for TCP, protocol used to transport our 
messages in the network.

bind() is used to associate a socket interface with port number, we have HOST set to standard 
IPV4 address, if it is a empty string then it will listen to all IPV4 interfaces.

# Logic for echo_server and echo_client
Our server creates a server at localhost:65000 and waits infinitely for a connection at that host 
and port and if connection recieved then it recieves data from the client and then stores that 
data and echo it back or we can say send that again to the client hence echoes the data.

Our client connects at the same port at which our server has established the connection and then
send some bytes object to the server and then recieves data from server and prints it, the client 
get what it has sent.