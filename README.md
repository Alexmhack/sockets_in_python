# sockets_in_python
using sockets module to interact with client and server

The module we use in python to deal with sockets is the socket module. Import socket and set
the HOST and PORT that our socket will be listening to, HOST = '127.0.0.1' OR localhost on our
local computer and the PORT = 65000 (non-privileged port), which means our socket will take
incoming connection from the address 127.0.0.1:65000

We will create a socket object using socket.socket() and socket type as socket.SOCK_STREAM.