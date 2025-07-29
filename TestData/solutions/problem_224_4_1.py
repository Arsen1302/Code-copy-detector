class Solution:
    def solution_224_4_1(self, num1: str, num2: str) -> str:
        
        NUMBERS = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

        def solution_224_4_2(num):
            num_integer = 0
            num_length = len(num) - 1
            for digit in num:
                num_integer += NUMBERS[digit] * 10 ** num_length
                num_length -= 1
            return num_integer

        return str(solution_224_4_2(num1) + solution_224_4_2(num2))