class Solution:
    def solution_1557_4(self, number: str, digit: str) -> str:
        return max (
            number[:i] + number[i+1:]
            for i in range(len(number))
            if number[i] == digit
        )