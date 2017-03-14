

case1 = open('F:\ipnu\python\projects\huawei\case.txt')
text = case1.read()
case1.close()
b = text.split('\n\n')


number = b[0].split()
NUMOFNETWORKNODES = number[0]  #网络节点数量
NUMOFNETWORKLINKS = number[1]  #网络链路数量
NUMOFCONNODES = number[2]      #消费节点数量

SERVERCOST = b[1]              #服务器部署成本

linkinfos = b[2].split('\n')        #链路信息

coninfos = b[3].split('\n')         #消费节点信息


networknodes = []
for i in range(int(NUMOFNETWORKNODES)):
	networknodes.append({'from':'','to':[],'bandwidth':[],'cost':[]})
	for linkinfo in linkinfos:
		linkinfo = list(map(eval, linkinfo.split()))            # string to int
		if linkinfo[0] == i:
			if linkinfo[0] != networknodes[i]['from']:
				networknodes[i]['from'] = linkinfo[0]
			networknodes[i]['to'].append(linkinfo[1])
			networknodes[i]['bandwidth'].append(linkinfo[2])
			networknodes[i]['cost'].append(linkinfo[3])
		if linkinfo[1] == i:
			if linkinfo[1] != networknodes[i]['from']:
				networknodes[i]['from'] = linkinfo[1]
			networknodes[i]['to'].append(linkinfo[0])
			networknodes[i]['bandwidth'].append(linkinfo[2])
			networknodes[i]['cost'].append(linkinfo[3])
			
print(networknodes)

connodes = []
for coninfo in coninfos:
	connodes.append(list(map(eval, coninfo.split())))
	
print(connodes)