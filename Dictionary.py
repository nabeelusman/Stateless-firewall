def dict():
    rules_dict = {'TCP':{},
                  'UDP': {},
                  'ICMP': {}}
    with open('ruleFile.txt') as f:
        num_lines = sum(1 for line in open('ruleFile.txt'))
        lines = f.readlines()
        for i in range(0, num_lines):
            rule = lines[i].translate(None, ')(').split("&&")
            #print rule
            a= rule[3].strip().split("|")
            #print a
            for proto in a:
                proto_value= proto.split("==")
                #print proto_value[1].strip()
                if proto_value[1].strip()=='TCP':
                    rules_dict['TCP'][str(i+1)] = {}
                    rules_dict['TCP'][str(i+1)]['IPS'] = rule[2].strip().split('|')[0].split('==')[1].strip().strip(')')
                    rules_dict['TCP'][str(i+1)]['IPD'] = rule[1].strip().split('|')[0].split('==')[1].strip().strip(')')
                    rules_dict['TCP'][str(i+1)]['PRT'] = rule[4].strip().split('|')[0].split('==')[1].strip().strip(')')
                    rules_dict['TCP'][str(i+1)]['ACT'] = rule[5].strip().split('|')[0].split('==')[1].strip().strip(')')
                    #print 'rules_dict: {}'.format(rules_dict)
                if proto_value[1].strip()=='UDP':
                    rules_dict['UDP'][str(i+1)] = {}
                    rules_dict['UDP'][str(i+1)]['IPS'] = rule[2].strip().split('|')[0].split('==')[1].strip().strip(')')
                    rules_dict['UDP'][str(i+1)]['IPD'] = rule[1].strip().split('|')[0].split('==')[1].strip().strip(')')
                    rules_dict['UDP'][str(i+1)]['PRT'] = rule[4].strip().split('|')[0].split('==')[1].strip().strip(')')
                    rules_dict['UDP'][str(i+1)]['ACT'] = rule[5].strip().split('|')[0].split('==')[1].strip().strip(')')
                    #print 'rules_dict: {}'.format(rules_dict)
                if proto_value[1].strip()=='ICMP':
                    rules_dict['ICMP'][str(i+1)] = {}
                    rules_dict['ICMP'][str(i+1)]['IPS'] = rule[2].strip().split('|')[0].split('==')[1].strip().strip(')')
                    rules_dict['ICMP'][str(i+1)]['IPD'] = rule[1].strip().split('|')[0].split('==')[1].strip().strip(')')
                    rules_dict['ICMP'][str(i+1)]['PRT'] = rule[4].strip().split('|')[0].split('==')[1].strip().strip(')')
                    rules_dict['ICMP'][str(i+1)]['ACT'] = rule[5].strip().split('|')[0].split('==')[1].strip().strip(')')
                    #print rules_dict

    return rules_dict
            # if 'TCP' == rule[3].strip().split('|')[0].split('==')[1].strip():
            #    # print rules_dict
            #     rules_dict['TCP'][str(i)] = {}
            #     rules_dict['TCP'][str(i)]['IPS'] = rule[2].strip().split('|')[0].split('==')[1].strip().strip(')')
            #     rules_dict['TCP'][str(i)]['IPD'] = rule[1].strip().split('|')[0].split('==')[1].strip().strip(')')
            #     rules_dict['TCP'][str(i)]['PRT'] = rule[4].strip().split('|')[0].split('==')[1].strip().strip(')')
            #     rules_dict['TCP'][str(i)]['ACT'] = rule[5].strip().split('|')[0].split('==')[1].strip().strip(')')
            #     print 'rules_dict: {}'.format(rules_dict)

#dict()