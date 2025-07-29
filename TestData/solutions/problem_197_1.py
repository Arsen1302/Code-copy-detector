class Solution:
    def solution_197_1(self, n: int) -> List[int]:
        return sorted([x for x in range(1,n+1)],key=lambda x: str(x))