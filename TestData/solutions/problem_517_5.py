class Solution:
    def solution_517_5(self, n: int) -> int:
        start = 1
        end = 1
        
        curr = 0
        res = 0
        
        while end <= n:
            curr += end
            while curr >= n:
                if curr == n:
                    res += 1
                curr -= start

                start += 1
            
            end += 1
        
        return res