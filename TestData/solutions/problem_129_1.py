class Solution(object):
    def solution_129_1(self, num):
        while num > 9:
            num = num % 10 + num // 10
        return num