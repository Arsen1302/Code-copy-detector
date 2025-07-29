class Solution:
    def solution_837_3(self, n: int) -> int:
        arr = list(map(int, str(n)))
        return prod(arr)-sum(arr)