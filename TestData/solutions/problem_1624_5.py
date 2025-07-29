class Solution:
    def solution_1624_5(self, s: str) -> str:
        res =[]
        for i in s:
            if i in res:
                return i 
                break 
            else:
                res.append(i)