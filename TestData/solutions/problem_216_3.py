class Solution:
    def solution_216_3(self, num: int) -> str:
        if num == 0:
            return "0"
        elif num < 0:
            num += 2 ** 32
            
        res = ""
        letter = "0123456789abcdef"
        while num > 0:
            res = letter[num % 16] + res
            num //= 16
        return res