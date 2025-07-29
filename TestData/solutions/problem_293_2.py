class Solution:
    def solution_293_2(self, num: int) -> str:
        answer = []
        sign = num

        if not num:
            return "0"
        elif num < 0:
            num *= -1

        while num:
            a = str(num % 7)
            answer.insert(0, a)
            num = num // 7

        if sign < 0:
            return "-" + "".join(answer)
        else:
            return "".join(answer)