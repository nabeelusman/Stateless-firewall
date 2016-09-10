from openpyxl import load_workbook
#from openpyxl.compat import *
import os
from ruleParser import protocolNumber
import logging
l = logging.getLogger("scapy.runtime")
l.setLevel(49)
from scapy.all import send, IP, TCP,ICMP,UDP


wb = load_workbook(filename=os.getcwd() + "/sample.xlsx")
# grab the active worksheet
# sheet = wb.active
sheet = wb['Test']
for row in sheet.rows:
	protocol = row[0].value
	if(protocol=='ICMP'):
		a=IP(src=row[1].value,dst=row[2].value,proto=protocolNumber(row[0].value))/ICMP()/TCP(sport=row[3].value,dport=row[4].value)/"Hello World"
		a.show()
		send(a)
	if (protocol == 'TCP'):
		a = IP(src=row[1].value, dst=row[2].value, proto=protocolNumber(row[0].value)) / TCP(
			sport=row[3].value, dport=row[4].value,flags='S',seq=42) / "Hello World"
		a.show()
		send(a)
	if (protocol == 'UDP'):
		a = IP(src=row[1].value, dst=row[2].value, proto=protocolNumber(row[0].value)) / UDP(
			sport=row[3].value, dport=row[4].value) / "Hello World"
		a.show()
		send(a)