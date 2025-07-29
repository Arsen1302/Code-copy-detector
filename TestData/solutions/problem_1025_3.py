class Solution:
    def solution_1025_3(self, low: int, high: int) -> int:
        if low%2==0 and high%2==0:
            return (high-low)//2
        if low%2==1 or high%2==1:
            return (high-low)//2+1