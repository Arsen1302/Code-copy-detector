class Solution:
    def solution_1503_3(self, s: str, t: str) -> int:
        a=Counter(s)
        b=Counter(t)
        
        count=0
        for i in set(s + t):
             count+=abs(a[i]-b[i])
        
        return count