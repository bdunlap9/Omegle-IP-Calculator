# [Weeke] -> Omegle IP Calculator

# Imports
import pyshark
import socket
import os

# Definitions
pcap_file = "C:\\Users\\Public\\Documents\\pcap_file.cap"
ip_file = "C:\\Users\\Public\\Documents\\ips.txt"

# Creating all needed files if they do not exist

# Create ip storage file if not exists
if not os.path.exists(ip_file):
    os.mkdir(ip_file)

# Start Pyshark capture & save pcap file after scanning for 5 mins
# interface = "Your network interface information"
capture = pyshark.LiveCapture(interface=r'Wi-Fi 3', output_file=pcap_file)
capture.sniff(timeout=100)
pkts = [pkt for pkt in capture._packets]
print(len(capture))
capture.close()

# PCAP file filter
cap = pyshark.FileCapture(pcap_file, display_filter="udp")
for pkt in cap:
    print(pkt.highest_layer)

# Filter out our IP
Our_IP = socket.gethostbyname(hostname)



# Calculate the most used source IP (AKA the most likely IP of the other user)
def most_likely(List):
    amount = 0
    victom_ip = List[0]

    for i in List:
        ip_list = List.count(i)
        
        if(ip_list > amount):
            amount = ip_list
            victom_ip = ip_list
    return victom_ip

# Display that IP to console
print("Most likely victom ip: ", victom_ip)

# Cleaning up generated files
if os.path.exists(pcap_file)
    os.remove(pcap_file)
if os.path.exists(ip_file)
    os.remove(ip_file)
