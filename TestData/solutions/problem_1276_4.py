class Solution:
    def solution_1276_4(self, s: str) -> int:
        counter = 0
        for i in range(len(s)-2):
            new = s[i:i+3]
            if len(new) == len(set(new)):
                counter = counter + 1
                
        return counter