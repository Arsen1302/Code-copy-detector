class Solution:
    def solution_1553_2(self, a: List[str], s: str) -> int:
        r=0
        for i in a:
            if len(i)<=len(s) and i==s[:len(i)]:
                r+=1
        return r