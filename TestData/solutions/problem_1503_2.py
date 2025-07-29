class Solution:
    def solution_1503_2(self, s: str, t: str) -> int:
        a=Counter(s)
        b=Counter(t)
        c=(a-b)+(b-a)
        
        count=0
        for i in c:
            count+=c[i]
        return count