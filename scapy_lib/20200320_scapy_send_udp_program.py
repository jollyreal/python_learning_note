from scapy.layers.inet import Ether
from scapy.layers.inet import IP
from scapy.layers.inet import UDP
from scapy.packet import Raw
from scapy.sendrecv import sendp

DESTINATION_MAC_ADDR = "11:22:33:44:55:66"
SOURCE_MAC_ADDR = "aa:bb:cc:dd:ee:ff"
DESTINATION_IP_ADDR = "192.168.0.100"
SOURCE_IP_ADDR = "192.168.0.123"
DESTINATION_PORT = 8080
SOURCE_PORT = 10430
RAW_DATA = "68656c6c6f20776f726c64" # hello world
NETWORK_INTERFACE = "Wi-Fi"

ether_frame = Ether(src=SOURCE_MAC_ADDR,dst=DESTINATION_MAC_ADDR)
ip_setting = IP(src=SOURCE_IP_ADDR,dst=DESTINATION_IP_ADDR)
udp_setting = UDP(dport=DESTINATION_PORT,sport=SOURCE_PORT)
udp_data = Raw(load=bytes.fromhex(RAW_DATA))
packet = ether_frame/ip_setting/udp_setting/udp_data

sendp(packet,iface=NETWORK_INTERFACE)