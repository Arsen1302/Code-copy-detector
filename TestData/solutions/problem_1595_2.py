class Solution:
    def solution_1595_2(self, num: int, k: int) -> int:
        if k%2 == 0 and num%2 != 0:
            return -1
        if num == 0:
            return 0
        elif k == 0 and num%10 == 0:
            return 1
        elif k == 0:
            return -1
        i = 1
        while True:
            if i*k > num:
                return -1
            if (i*k)%10 == num%10:
                return i
            i += 1