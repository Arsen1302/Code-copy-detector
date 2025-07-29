class Solution:
    def solution_686_5_1 (self):
        self.base_cases = [1, 2, 6, 7]
        self.offsets = [2, 2, -1, 1]
        
    def solution_686_5_2(self, n: int) -> int:
        if n <= 4:
            return self.base_cases [n - 1]

        return n + self.offsets[(n + 3) % 4]