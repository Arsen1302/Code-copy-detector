class Solution:
    def solution_701_5(self, s: str) -> str:
        res = []
        curOpen = 0
        for c in s:
            if c == '(':
                if curOpen:
                    res.append(c)
                curOpen += 1
            else:
                curOpen -= 1
                if curOpen:
                    res.append(c)
        
        return ''.join(res)