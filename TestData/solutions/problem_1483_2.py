class Solution:
    def solution_1483_2(self, num: int) -> int:
        num = sorted(str(num),reverse=True)
        return int(num[0]) + int(num[1]) + int(num[2])*10 + int(num[3])*10