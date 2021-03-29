import time
import socket

site = input("Enter the site: ")
url = input("Enter the URL: ")
port = int(input("Enter the port: "))

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect((site, port))
msg = "GET {} HTTP/1.0\r\nhost: {}\n\n".format(url, site)
print(msg)
mysocket.send(msg.encode())

picture = b''
count = 0

while True:
	data = mysocket.recv(1024*5)
	if len(data) < 1:
		break
	time.sleep(0.25)
	print( len(data) , count)
	count += len(data)
	picture += data
mysocket.close()

picture = picture[picture.find(b"\r\n\r\n")+4:]
fhand = open("pic.jpg", 'wb')
fhand.write(picture)
fhand.close()