class Solution:
    def solution_1498_5(self, num: int) -> int:
        if sum(map(int,str(num))) % 2 == 0:
            return num//2
        return (num-1)//2