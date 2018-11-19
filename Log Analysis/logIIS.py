from collections import Counter
def getIPAddress():
	ipAddress = []
	with open('iis.log','r') as inf:
		for line in inf:
			ip = line.split(' ')[1]
			if ip not in ipAddress:
				ipAddress.append(ip)
	print('* Unique Ip Address: {0}'.format(len(ipAddress)))

def countLines():
	totalLines = 0
	with open('iis.log', 'r') as inf:
		for line in inf:
			totalLines += 1
	print('* Total requests: {0}'.format(totalLines))


"""
This had issue so instead I just did CTRL+F " 500"
"""
def countError():
	with open('iis.log','r') as inf:
		count = 0
		for line in inf:
			if line.split(' ')[3] == '500':
				count += 1
				print(line.split(' ')[3])



def countCommonIP():
	ipAddresses = []
	with open('iis.log', 'r') as inf:
		for line in inf:
			ipAddresses.append(line.split(' ')[1])
	data = Counter(ipAddresses)
	print(data.most_common)

def countCommonHours():
	hours = []
	with open('iis.log','r') as inf:
		for line in inf:
			hours.append(line.split(':')[0])
	data = Counter(hours)
	print(data.most_common)

getIPAddress()
countLines()
print('\n--------------------')
countCommonIP()
print('\n--------------------')
countCommonHours()
