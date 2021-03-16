import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(3)
host = input("[*] Give ip-Address: ")  # '192.168.0.6'
port = int(input("[*] Give a port number: "))  # 445,135,1024,139


def portScanner(port):
    if (sock.connect_ex((host, port))):
        print(port, "is closed ")
    else:
        print(port, "is open ")


if __name__ == '__main__':
    portScanner(port=port)
