class Solution:
    def solution_265_5(self, ip):
        ip_dot = ip.split('.')
        if len(ip_dot)>1:
            if len(ip_dot) == 4:
                for x in ip_dot:
                    if len(x)>1 and x[0] == '0':
                        return "Neither"
                    if not x.isnumeric() or int(x)>255:
                        return "Neither"
            else:
                return "Neither"
        
            return "IPv4"
    
        else:
            ip_colon = ip.split(':')
            for x in ip_colon:
                if len(ip_colon) == 8:
                    for y in x:
                        if y.isalpha() and y.lower() not in ['a', 'b', 'c', 'd', 'e', 'f']:
                            return "Neither"
                else:
                    return "Neither"

                if not x or not x.isalnum() or len(x) > 4:                        
                    return "Neither"
            
            return "IPv6"