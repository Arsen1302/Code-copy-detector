class Solution:
    def solution_1572_2(self, s: str, letter: str) -> int:
        c=0
        for i in s:
            if i==letter:
                c+=1
        n=len(s)
        return int(c/n*100)