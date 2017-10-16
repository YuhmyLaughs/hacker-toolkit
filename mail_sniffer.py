from scapy.all import *

#callback for all the packages that match the filter
def packet_callback(packet):
	print packet.show()

#trigger the sniffer
sniff(prn=packet_callback,count=1)
