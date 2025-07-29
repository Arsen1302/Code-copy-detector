class Solution:
    def solution_1250_2(self, n: int, k: int) -> int:
        output_sum = 0
        while (n > 0) :
            rem = n % k
            output_sum = output_sum + rem 
            n = int(n / k)
        return output_sum