import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
HOST_NAME=socket.gethostname()

PORT=12345
s.bind((HOST_NAME,PORT))
s.listen(4)


while True:
    client,address=s.accept()
    client.send(bytes("hello,how r u?","utf-8"))
    print("client is connected and has the address",address)
