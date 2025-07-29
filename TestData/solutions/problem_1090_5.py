class Solution:
    def solution_1090_5(self, s: str) -> int:
        
        num = maxnum = 0
        for char in s:
            num += (char == "(") - (char == ")")
            maxnum = num if num > maxnum else maxnum
        
        return maxnum