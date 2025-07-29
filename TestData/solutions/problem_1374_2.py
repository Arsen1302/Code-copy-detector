class Solution:
    def solution_1374_2(self, operations: List[str]) -> int:
        return sum(1 if '+' in o else -1 for o in operations)