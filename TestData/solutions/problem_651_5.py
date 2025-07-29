class Solution:
    def solution_651_5(self, x: int, y: int, bound: int) -> List[int]:
        xset, yset = set(), set()
        for i in range(20):
            if x**i < bound:
                xset.add(x**i)
        
        for i in range(20):
            if y**i < bound:
                yset.add(y**i)
        
        ans = set()
        for i in xset:
            for j in yset:
                if i+j <= bound:
                    ans.add(i+j)
        
        return list(ans)