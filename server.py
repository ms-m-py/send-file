
import socket
ip = socket.gethostbyname(socket.gethostname())
port = 9999
addr=(ip,port)
format="utf-8"
print("server started")
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(addr)
server.listen()
print("is listening")
data=b""
while True:
    conn,addr=server.accept()
    print(f"new connection {addr}")
    file_name=conn.recv(1024).decode()
    if file_name:
        conn.send("1".encode(format))
        while 1:
            try:
                file_data=conn.recv(1024)
                if not file_data:
                    print("break")
                    break
                data+=file_data
            except:
                print("break2")
                break
    file=open(file_name,"wb")
    file.write(data)
    file.close()
    print(f" {file_name}resived")
