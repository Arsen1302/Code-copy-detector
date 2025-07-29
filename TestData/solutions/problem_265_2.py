class Solution:
    def solution_265_2(self, queryIP: str) -> str:
        letterHashSet = ('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','A','B','C','D','E','F')
        
        ipv4 = queryIP.split('.')
        ipv6 = queryIP.split(':')
        
        if len(ipv4) == 1:
            if len(ipv6) != 8:
                return "Neither"
            else:
                for i in ipv6:
                    if len(i) > 4 or len(i) == 0:
                        return "Neither"
                    for char in i:
                        if char not in letterHashSet:
                            return "Neither"
                return "IPv6"
        else:
            if len(ipv4) != 4:
                return "Neither"
            else:
                for i in ipv4:
                    if (len(i) > 1 and i[0] == '0') or not i.isdigit() or int(i) < 0 or int(i) > 255:
                        return "Neither"
                return "IPv4"