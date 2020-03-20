# How to use scapy to send a UDP packet

According to the OSI model, UDP is located at transport layer (layer 4). if we want to send a packet we can use scapy to set the detail from layer 1 to layer 4. 

## 1. Physical Layer and Data-Link Layer
set the **destination MAC address** and **source MAC address** through [scapy Ether](https://scapy.readthedocs.io/en/latest/api/scapy.layers.inet.html#scapy.layers.inet.IP)

```python
from scapy.layers.inet import Ether
DESTINATION_MAC_ADDR = "11:22:33:44:55:66"
SOURCE_MAC_ADDR = "aa:bb:cc:dd:ee:ff"
ether_frame = Ether(src=SOURCE_MAC_ADDR,dst=DESTINATION_MAC_ADDR)
```

## 2. Network Layer
set the **destination IP address** and **source IP address** through [scapy IP](https://scapy.readthedocs.io/en/latest/api/scapy.layers.inet.html#scapy.layers.inet.IP)

```python 
from scapy.layers.inet import IP
DESTINATION_IP_ADDR = "192.168.0.100"
SOURCE_IP_ADDR = "192.168.0.123"
ip_setting = IP(src=SOURCE_IP_ADDR,dst=DESTINATION_IP_ADDR)
```

## 3. Transport layer
set the **destination port** and **source port** through [scapy UDP](https://scapy.readthedocs.io/en/latest/api/scapy.layers.inet.html#scapy.layers.inet.UDP)


```python
from scapy.layers.inet import UDP
DESTINATION_PORT = 8080
SOURCE_PORT = 10430
udp_setting = UDP(dport=DESTINATION_PORT,sport=SOURCE_PORT)
```

## 4. UDP load
set the udp payload through [scapy Raw](https://scapy.readthedocs.io/en/latest/api/scapy.packet.html#scapy.packet.Raw)

```python
from scapy.packet import Raw
RAW_DATA = "68656c6c6f20776f726c64" # hello world
udp_data = Raw(load=bytes.fromhex(RAW_DATA))
```

## 5. Combine all the layer
combine setting in step 1~4 to form a packet

```python
packet = ether_frame/ip_setting/udp_setting/udp_data
```

## 6. send out the packet
use [scapy sendp](https://scapy.readthedocs.io/en/latest/api/scapy.sendrecv.html#scapy.sendrecv.sendp) to set the interface and send the packet

```python
from scapy.sendrecv import sendp
NETWORK_INTERFACE = "Wi-Fi"
sendp(packet,iface=NETWORK_INTERFACE)
```

## Finish
you can use wireshark to confirm the packet had really been sent out.
