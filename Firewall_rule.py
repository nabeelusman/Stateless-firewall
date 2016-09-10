import re
from inputCheck import *
import fileinput
from tempfile import mkstemp
from shutil import move
from os import remove, close


def addRule() :
    print "Rule format :(ip.dst == 192.168.175.123) && (ip.src == 192.178.155.155) && (Protocol == TCP | Protocol ==UDP) && (port==12345)"
    print "operators: AND > && , OR > || , not > !"

    user_input = raw_input("Please enter the rule in above format \n")
    input = user_input.translate(None, ')(')
    print input
    tokens = re.split('&& | \| | \!', input)
    tokenLength = tokens.__len__()
    for i in range(0, tokenLength):
        valueCheck = tokens[i].split('==')

        if valueCheck[0].strip(" ") == 'ip.dst' or valueCheck[0].strip(" ") == 'ip.src':
            checkAddress = ip_checkv4(valueCheck[1])
            if checkAddress == False :
                addRule()

        elif valueCheck[0].strip(" ") == 'Protocol':
            checkProto = checkProtocol(valueCheck[1].strip(" "))
            if checkProto == False:
                print "Please check the input protocol"
                addRule()

        elif valueCheck[0].strip(" ") == 'port':
            checkPort = checkPorts(valueCheck[1].strip(" "))
            if checkPort == False:
                addRule()
        else:
            print 'Please enter a valid rule'
            addRule()
        print valueCheck

    readLine = open("ruleFile.txt",  "r")
    lines = sum(1 for line in readLine)
    '''print lines'''
    ruleLine = str(lines+1)
    target =  raw_input("Please enter PASS or DROP for the above rule \n")
    input = ruleLine + " && " + user_input + " && act == " + target


    writeFile = open("ruleFile.txt", "a")
    writeFile.writelines(input + '\n')


'''def deleteRule():
    print "delete rule"

def modifyRule():
    viewFile = open("ruleFile.txt", "r")
    print viewFile.read()
    rulenumber = raw_input("Please enter the rule number \n")
    viewFile = open("ruleFile.txt", "r")
    for line in viewFile:
        print line
        if line.__contains__(rulenumber):
            modifiedRule = rulenumber + " && " + raw_input("Please enter the modified rule\n")
            print modifiedRule
            file = open("ruleFile.txt", "a")
            replace("/Users/Nabeel/PycharmProjects/firewall/ruleFile.txt",line, modifiedRule)


def replace(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    close(fh)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)'''



def showRule():
    viewFile = open("ruleFile.txt", "r")
    print viewFile.read()
    viewFile.close()



def rule_action():
    action = raw_input("Please enter your rule action : A > Add rule ; S > Show rules; E > Exit\n")
    if action == "A":
        addRule()
    elif action == "D":
        deleteRule()
    elif action == "M":
        modifyRule()
    elif action == "S":
        showRule()
    elif action == "E":
	exit(0)

while True:
    rule_action()


'''def activate_rule():'''









