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