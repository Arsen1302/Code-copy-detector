class Solution:
    def solution_669_3(self, A: List[int], K: int) -> List[int]:
        return list(str(int("".join([str(i) for i in A])) + K))