from socket import socket, AF_INET, SOCK_DGRAM
from scapy.all import IP, UDP, Raw, sniff

IP_ADDRESS = '127.0.0.1'
PORT = 55555


def filter_packet(packet):
    return IP in packet and packet[IP].src == IP and UDP in packet and packet[UDP].sport == PORT

def main():
    with socket(AF_INET, SOCK_DGRAM) as client_socket:
        data = input("What whould you like to send? ")
        data = data.encode()

        client_socket.sendto(data, (IP_ADDRESS, PORT)) 

        data = client_socket.recvfrom(1024)
        
        flow = []
        answers = {}

        while True:
            packet = sniff(count = 1)
            
            check = False
            if len(flow) == 0:
                check = True
            elif flow[-1] == packet[IP].id:
                check = True

            if check:
                index = packet[IP].frag
                data = packet[Raw].load
                
                answers[index] = data

                if packet[IP] != 'MF':
                    break
                flow.append(packet[IP].id)

        sorted_answers = dict(sorted(answers.items()))

        message = ''.join(sorted_answers.values())

        print(message)


if __name__ == "__main__":
    main()