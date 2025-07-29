class Solution:
    def solution_44_5_1(self, s: str) -> List[List[str]]:
        res, part = [], []
        
        def solution_44_5_2(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if solution_44_5_3(s, i, j):
                    part.append(s[i:j+1])
                    solution_44_5_2(j + 1)
                    part.pop()
        solution_44_5_2(0)
        return res
    
def solution_44_5_3( s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True