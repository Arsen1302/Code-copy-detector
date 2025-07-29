class Solution:
    def solution_1025_2(self, low: int, high: int) -> int:
        val=(high-low+1)//2
        return val+1 if(low&amp;1 and high&amp;1) else val