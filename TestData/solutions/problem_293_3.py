class Solution:
    def solution_293_3(self, num: int) -> str:
        answer = ""
        sign = num

        if not num:
            return "0"
        elif num < 0:
            num *= -1

        while num:
            a = str(num % 7)
            answer = a + answer
            num = num // 7

        if sign < 0:
            answer = "-" + answer

        return answer