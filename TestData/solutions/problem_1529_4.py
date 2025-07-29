class Solution:
    def solution_1529_4(self, start: int, goal: int) -> int:
        a = bin(start)[2:]
        c = bin(goal)[2:]
        new_a = '0' * (32 - len(a)) + a
        new_c = '0' * (32 - len(c)) + c
        c = 0
        for i in range(len(new_a)):
            if new_a[i] != new_c[i]:
                c = c +1
        return c