class Solution:
    def solution_1498_2(self, num: int) -> int:
        count = 0
        for i in range(num+1):
            sum_of_digits = sum(int(digit) for digit in str(i)) 
            if sum_of_digits % 2 == 0 and sum_of_digits != 0:
                count += 1
        return count