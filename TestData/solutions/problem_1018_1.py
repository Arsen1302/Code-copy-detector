class Solution:
    def solution_1018_1(self, s: str) -> int: 
            res = 0
            s = s.split("0")

            for one in s:
                if one == "":
                    continue
                    
                n = len(one)
                temp = (n / 2)*(2*n + (n-1)*-1)
                    
                if temp >= 1000000007:
                    res += temp % 1000000007
                else:
                    res += temp
            return int(res)