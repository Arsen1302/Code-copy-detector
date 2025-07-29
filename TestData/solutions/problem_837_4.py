class Solution:
    def solution_837_4(self, n: int) -> int:
        arr = list(map(int, str(n)))
        return reduce(operator.mul, arr) - sum(arr)