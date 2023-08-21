import socket
import time 

host = '0.0.0.0' # Listen on all available interfaces
port = 12345     # Use port 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
print(f"Listening on {host}:{port}")
conn, addr = s.accept()
print(f"Connection from {addr}")

li = ["o", "p"]
while True:
    for i in li:
        send = i
        print(send)
        conn.sendall(send.encode())
        time.sleep(15)
        

conn.close()