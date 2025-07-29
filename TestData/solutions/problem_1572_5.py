class Solution:
    def solution_1572_5(self, s: str, letter: str) -> int: 
        c=0
        for i in s:
            if i==letter:
                c+=1
        a=(c/len(s))*100
        return int(a)