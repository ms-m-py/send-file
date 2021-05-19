import socket
ip = socket.gethostbyname(socket.gethostname())
port = 9999
addr=(ip,port)
format="utf-8"
file_name=input("file_name")
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(addr)
file=open(file_name,"rb")
client.send(file_name.encode(format))
a=client.recv(1024).decode()
if a:
    while 1:
        data=file.read(1024)
        if not data:
            break
        client.send(data)
