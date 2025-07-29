class Solution:
    def solution_669_2(self, num: List[int], k: int) -> List[int]:
        return [int(i) for i in str(int(''.join([str(i) for i in num]))+k)]