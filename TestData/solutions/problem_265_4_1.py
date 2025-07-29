class Solution:
    def solution_265_4_1(self, queryIP: str) -> str:
        
        # IPv4 checks
        
        def solution_265_4_2(addr):
            return addr.isdigit() and int(addr)>=0 and int(addr)<=255
        
        def solution_265_4_3(addr):
            return addr.isdigit() and ((len(addr) > 1 and addr[0] != "0") or len(addr) == 1)

        def solution_265_4_4(ip):
            return len(ip) == 4

        def solution_265_4_5(arr):
            return solution_265_4_4(arr) and all([solution_265_4_2(addr) and solution_265_4_3(addr) for addr in arr])
        
        # IPv6 checks
        
        def solution_265_4_6(addr):
            addr = addr.strip()
            return len(addr) >= 1 and len(addr) <= 4
        
        def solution_265_4_7(addr):
            valid_alpha_set = set("abcdefABCDEF")
            for c in addr:
                if (
                    (not c.isdigit() and not c.isalpha()) or 
                    (c.isalpha() and c not in valid_alpha_set)
                ):
                    return False
            return True
        
        def solution_265_4_8(ip):
            return len(ip) == 8

        def solution_265_4_9(arr):            
            return solution_265_4_8(arr) and all([solution_265_4_6(addr) and solution_265_4_7(addr) for addr in arr])
        
        # Main IP format solution_265_4_10
        
        def solution_265_4_10(queryIP):
            if solution_265_4_5(queryIP.split(".")):
                return "IPv4"
            elif solution_265_4_9(queryIP.split(":")):
                return "IPv6"        
            else:
                return "Neither"  
        
        return solution_265_4_10(queryIP)