class Solution:
    def solution_669_1(self, num: List[int], k: int) -> List[int]:
        return list(str(int("".join([str(x) for x in num])) + k))