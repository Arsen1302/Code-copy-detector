class Solution:
    def solution_440_5(self, n: int) -> int:
        digits = [int(d) for d in str(n)]

        if len(digits) == 1:
            return n

        l = 0
        for i in range(1,len(digits)):
            if digits[i] > digits[i-1]:
                l = i
            elif digits[i] < digits[i-1]:
                digits[l] -= 1
                for j in range(l+1,len(digits)):
                    digits[j] = 9
                break
        if digits[0] == 0:
            digits.pop(0)

        return int("".join([str(d) for d in digits]))