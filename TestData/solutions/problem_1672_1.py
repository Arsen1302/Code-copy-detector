class Solution:
    def solution_1672_1(self, s: str) -> int:

        arr = ''.join(['1' if ord(s[i])-ord(s[i-1]) == 1 
                       else ' ' for i in range(1,len(s))]).split()
                       
        return max((len(ones)+1 for ones in arr), default = 1)