class Solution:
    def solution_180_3(self, n: int) -> int:
        count = 1
        for i in range(n):
            count += 9*math.factorial(9)/math.factorial(9-i)
        return int(count)