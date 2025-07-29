class Solution:
    def solution_412_3(self, s: str) -> int:
        prev , curr , res = 0 , 1 , 0
        
        for i in range(1,len(s)):
            if s[i-1] == s[i]:
                curr +=1
            else:
                prev = curr
                curr = 1
            if prev >= curr:
                res+=1
        return res