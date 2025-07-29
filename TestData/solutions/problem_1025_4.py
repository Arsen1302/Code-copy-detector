class Solution:
    def solution_1025_4(self, low: int, high: int) -> int:
        if(low%2==0 and high%2==0):
            return (high-low)//2
        else:
            return (high-low)//2 + 1