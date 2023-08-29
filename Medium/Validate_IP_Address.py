"""
Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.
A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses while "192.168.01.1", "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses.
A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

1 <= xi.length <= 4
xi is a hexadecimal string which may contain digits, lowercase English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
Leading zeros are allowed in xi.
For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.
Example 1:
Input: queryIP = "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".

Example 2:
Input: queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"
Explanation: This is a valid IPv6 address, return "IPv6".

Example 3:
Input: queryIP = "256.256.256.256"
Output: "Neither"
Explanation: This is neither a IPv4 address nor a IPv6 address. 
"""

def validateIpaddress(queryIP):
    def valid_ip4(s):
        parts=s.split('.') #"192.168.1.1"   ['192', '168','1','1']
        
        if len(parts)!=4:
            return False
        
        for i in parts:
            if not i.isdigit() or not 0 <= int(i) <=255 or (len(i)>1 and i[0]=='0'):
                return False
        return True
        
    
    def valid_ip6(s):
        ip_list=s.split(':')
        if len(ip_list)!=8:
            return False
        
        for j in ip_list:
            if not ( 1 <= len(j)<=4 ) or any(c not in '0123456789abcdefABCDEF' for c in j):
                return False
        return True    
    
    if '.' in queryIP and valid_ip4(queryIP):
        return "IPv4"
    elif ':'in queryIP and valid_ip6(queryIP):
        return "IPV6"
    else:
        return "Neither"
            
print(validateIpaddress('192.168.1.1')) 
print(validateIpaddress('2001:0db8:85a3:0000:0000:8a2e:0370:7334'))  # IPv6
print(validateIpaddress('256.256.256.256'))  # Neither
print(validateIpaddress('2001:0db8:85a3::8A2E:037j:7334'))  # Neither

