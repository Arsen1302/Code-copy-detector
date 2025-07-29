class Solution:
    def solution_869_5(self, a: int, b: int, c: int) -> int:
        ans=0
        for i in range(32):
            bit_a = (a&amp;(1<<i)) >> i
            bit_b = (b&amp;(1<<i)) >> i
            bit_c = (c&amp;(1<<i)) >> i
            if bit_a | bit_b != bit_c:
                ans+=max(1,bit_a + bit_b)
            else:
                continue
        return ans