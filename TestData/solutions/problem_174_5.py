class Solution:
    def solution_174_5(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            s[i],s[-i-1]=s[-i-1],s[i]
        return s