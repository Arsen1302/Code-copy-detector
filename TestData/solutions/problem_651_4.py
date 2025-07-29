class Solution:
    def solution_651_4(self, x: int, y: int, bound: int) -> List[int]:
        d = {}
        a = 1
        
        while a < bound:
            b = 1
            while True:
                if a + b <= bound:
                    d[a+b] = True
                    b*=y
                    if y == 1: break
                else:
                    break
            a *= x
            if x == 1: break
        
        ans = []
        for i in d : ans.append(i)
        return ans