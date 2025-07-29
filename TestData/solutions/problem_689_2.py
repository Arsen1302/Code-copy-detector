class Solution:
    def solution_689_2(self, N: int) -> int:
        sum_ = 1
        
        while N > sum_:
            sum_ = sum_ * 2 + 1
        
        return sum_ - N