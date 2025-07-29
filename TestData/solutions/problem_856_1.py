class Solution:
    def solution_856_1(self, n: int) -> List[int]:
        return list(range(1,n))+[-n*(n-1)//2]