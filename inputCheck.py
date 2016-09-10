def checkProtocol(protocol):
    protocols = ['ICMP', 'TCP','UDP']
    if(protocol in protocols):
        return True
    else:
        return False

def checkTokens(tokens,n):
    check = True
    for i in range(0,n):
        if(i%2==0):
            if(not(tokens[i]=='-p' or tokens[i]=='-s' or tokens[i]=='-d' or tokens[i]=='-sport' or tokens[i]=='-dport' or tokens[i]=='-tar')):
                print tokens[i] +" is not a valid option. Please use a valid option"
                check = False
    return check

def checkPorts(port):
    if(port == 'any'):
	return True
    else:
	port= int(port)
	if(port<0 or port>65535):
	        print "Port number should be within the range 0-65535"
	        return False
        else:
	        return True

def ip_checkv4(ip):
    parts = ip.split(".")
    if len(parts) < 4 or len(parts) > 4:
        print "Invalid IP length should be 4 not greater or less than 4"
        return False
    else:
        while len(parts) == 4:
            a = int(parts[0])
            b = int(parts[1])
            c = int(parts[2])
            d = int(parts[3])
            if a <= 0 or a == 127:
                print "Invalid IP address"
                return False
            elif d == 0:
                print "Invalid IP address. Host id  should not be 0 or less than zero "
                return False
            elif a >= 255:
                print "Invalid IP address. It should not be 255 or greater than 255 or less than 0 A"
                return False
            elif b >= 255 or b < 0:
                print "Invalid IP address. It should not be 255 or greater than 255 or less than 0 B"
                return False
            elif c >= 255 or c < 0:
                print "Invalid IP address. It should not be 255 or greater than 255 or less than 0 C"
                return False
            elif d >= 255 or c < 0:
                print "Invalid IP address. It should not be 255 or greater than 255 or less than 0 D"
                return False
            else:
                return True

def checkTarget(target):
    check = True
    if(target!='PASS' and target!='DROP'):
        print 'Invalid target.'
        check = False
    return check
