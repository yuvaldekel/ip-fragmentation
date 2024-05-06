from socket import socket, AF_INET, SOCK_DGRAM
#from scapy.all import *

IP = '127.0.0.1'
PORT = 55555

def main():
    with socket(AF_INET, SOCK_DGRAM) as client_socket:
        data = input("What whould you like to send? ")
        data = data.encode()

        client_socket.sendto(data, (IP, PORT)) 
        

if __name__ == "__main__":
    main()