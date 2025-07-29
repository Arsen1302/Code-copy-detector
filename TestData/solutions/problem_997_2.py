class Solution:
    def solution_997_2(self, n: int, start: int) -> int:
        return reduce(operator.xor,[start+(2*i) for i in range(n)])