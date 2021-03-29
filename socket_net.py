import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(("data.pr4e.org",80))
msg = "GET /remote.txt HTTP/1.0\n\n".encode()
mysocket.send(msg)

while True:
	data = mysocket.recv(1024)
	if len(data) < 1:
		break
	print(data.decode(), flush=True)

mysocket.close()