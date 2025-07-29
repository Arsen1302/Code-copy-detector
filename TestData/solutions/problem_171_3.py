class Solution:
    def solution_171_3(self, n: int) -> List[int]:
        return [(bin(i)[2:]).count("1") for i in range(n+1)]