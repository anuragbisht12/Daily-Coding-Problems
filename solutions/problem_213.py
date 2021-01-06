def generate_valid_ips(string, curr, all_ips):
    if len(curr) > 4 or (len(curr) < 4 and not string):
        return
    elif len(curr) == 4 and not string:
        all_ips.add(".".join(curr))
        return

    def recurse(index):
        generate_valid_ips(string[index:], curr + [string[0:index]], all_ips)

    recurse(1)
    first = int(string[0])
    if first and len(string) > 1:
        recurse(2)
        if len(string) > 2 and first < 3:
            recurse(3)


def generate_valid_ip_helper(string):
    all_ips = set()
    generate_valid_ips(string, list(), all_ips)
    return all_ips


# Tests
assert generate_valid_ip_helper("2542540123") == \
    {'254.25.40.123', '254.254.0.123'}
assert generate_valid_ip_helper("0000") == \
    {'0.0.0.0'}
assert generate_valid_ip_helper("255255255255") == \
    {'255.255.255.255'}
assert generate_valid_ip_helper("100100110") == \
    {'100.10.0.110', '10.0.100.110', '100.100.11.0', '100.100.1.10'}


"""
New way
"""

"""
string: 1921680
O/P: [
    1.9.216.80
    1.92.16.80
    1.92.168.0
    19.2.168.0
    19.21.6.80
    19.21.68.0
    19.216.8.0
    192.1.6.80
    192.1.68.0
    192.16.8.0

]

"""

# O(1) time and O(1) space
def validIPAddresses(string):
    # Write your code here.
	ipAddressesFound=[]
	
	for i in range(1,min(len(string),4)):
		currentIPAddressParts=["","","",""]
		
		currentIPAddressParts[0]=string[:i]
		if not isValidPart(currentIPAddressParts[0]):
			continue
			
		for j in range(i+1,i+min(len(string)-i,4)):
			currentIPAddressParts[1]=string[i:j]
			if not isValidPart(currentIPAddressParts[1]):
				continue
				
			for k in range(j+1,j+min(len(string)-j,4)):
				currentIPAddressParts[2]=string[j:k]
				currentIPAddressParts[3]=string[k:]
				
				if isValidPart(currentIPAddressParts[2]) and isValidPart(currentIPAddressParts[3]):
					ipAddressesFound.append(".".join(currentIPAddressParts))
	
    return ipAddressesFound

def isValidPart(string):
	stringAsInt=int(string)
	if stringAsInt>255:
		return False
	
	return len(string)==len(str(stringAsInt)) #check for leading zeros

