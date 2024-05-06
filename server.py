from scapy.all import IP, UDP, Raw, send
from socket import socket, AF_INET, SOCK_DGRAM
from fragmentation import fragment_string

PORT = 55555

def main():
    with socket(AF_INET, SOCK_DGRAM) as server_socket:
        server_socket.bind(('0.0.0.0', PORT))
        
        (client_data, client_address) = server_socket.recvfrom(1024)
        client_data = client_data.decode()
        data_fragments = fragment_string(client_data)

        print(data_fragments)
        client_ip, client_port = client_address

        length = len(data_fragments)
        for index, data_fragments in enumerate(data_fragments):
            i_packet = IP(dst = client_ip, frag = index, id = 1, proto = 'udp')/UDP(dport = client_port, sport = PORT)/Raw(data_fragments)

            if index + 1 != length:
                i_packet[IP].flags = "MF"

            #i_packet.show()
            send(i_packet, iface = 'wlp4s0')    

if __name__ == "__main__":
    main()