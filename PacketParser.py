import logging
from scapy.layers.inet import *
from Dictionary import dict

l = logging.getLogger()
# l.setLevel(49)
#from openpyxl import load_workbook
import nfqueue
from scapy.all import *
from ruleParser import *

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log= logging.getLogger(__name__)
def process(i, payload):
    dictionary = dict()
    log.info("dictionary: %s", dictionary)
    #print dictionary

    print "Got dictionary"
    data = payload.get_data()
    pkt= IP(data)
    protocol=pkt.proto
    source = pkt.src
    dest = pkt.dst
    packetDrop = True
    pkt=TCP(data)
    dport = pkt.dport
    i=0
    for packet in pkt:
        pkt_protocol= returnProtocol(protocol)
        rules_proto= dictionary[pkt_protocol]
        if(rules_proto == {}):
            payload.set_verdict(nfqueue.NF_DROP)
            print 'drop packet from empty set'
        else:
            for rule in rules_proto:
                src_flag=True
                dst_flag= True
                port_flag= True
                action_flag= True
                log.info("rule: %s", rule)
                src_flag=isMatch(rules_proto[rule]['IPS'],source)
                dst_flag= isMatch(rules_proto[rule]['IPD'],dest)
                port_flag= isMatch(rules_proto[rule]['PRT'],dport)
                action_flag= isDrop(rules_proto[rule]['ACT'])
                log.info("src_flag: %s .. dst_flag: %s .. port_flag: %s .. action_flag: %s", src_flag, dst_flag, port_flag, action_flag)
                if (src_flag and dst_flag and port_flag and action_flag):
                    payload.set_verdict(nfqueue.NF_DROP)
                    print 'drop packet'
		    return 	
                else:
                    payload.set_verdict(nfqueue.NF_ACCEPT)
                    print 'accept packet'





        #print protocol



def startFirewall():
    print 'Starting the Firewall'	
    q = nfqueue.queue()
    q.open()
    q.bind(socket.AF_INET)
    q.set_callback(process)
    q.create_queue(0)
    try:
        q.try_run()
    except KeyboardInterrupt:
        print "Exiting..."
        q.unbind(socket.AF_INET)
        q.close()
        sys.exit(0)

startFirewall()
