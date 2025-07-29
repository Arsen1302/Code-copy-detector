class Solution:
    def solution_1165_1(self, encoded: List[int], first: int) -> List[int]:
        return [first] + [first:= first ^ x for x in encoded]