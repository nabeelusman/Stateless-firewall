def isMatch(ruleValue,packetvalue ):
    if(ruleValue == 'any'):
        return True
    else:
        return ruleValue == packetvalue


def isSource(ruleSrc, packetSrc):
    if(ruleSrc=='any'):
        return True
    else:
        return ruleSrc == packetSrc

def isDest(ruleDest, packetDest):
    if (ruleDest == 'any'):
        return True
    else:
        return ruleDest == packetDest

# def isSport(ruleSport, packetSport):
#     if (ruleSport == 'any'):
#         return True
#     else:
#         return ruleSport == packetSport

def isDport(ruleDport, packetDport):
    if (ruleDport == 'any'):
        return True
    else:
        return ruleDport == packetDport

def isDrop(ruleDrop):
    if(ruleDrop=='DROP'):
        return True
    elif(ruleDrop=='PASS'):
        return False

def isProtocol(ruleProtocol,pktProtocol):
    if(ruleProtocol=='any'):
        return True
    else:
        protocol= {'ICMP': 1,'IGMP': 2,'TCP':6, 'UDP':17}
        return pktProtocol==protocol[ruleProtocol]

def returnProtocol(protocols):
        protocol= {1: 'ICMP',6:'TCP', 17:'UDP'}
        return protocol[protocols]


def protocolNumber(protocols):
    protocol = {'ICMP': 1,'TCP': 6,'UDP': 17}
    return protocol[protocols]
