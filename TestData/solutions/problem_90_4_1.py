class Solution:
    def solution_90_4_1(self, left: int, right: int) -> int:
        
        def solution_90_4_2(left, right, p):
            d = right - left
            x = 1 << p
            if d >= x:
                return 0
            else:
                return 1 if right &amp; x != 0 else 0
        
        ans = left
        
        for i in range(32):
            if ans &amp; (1 << i) and not solution_90_4_2(left, right, i):
                ans ^= (1 << i)
        
        return ans