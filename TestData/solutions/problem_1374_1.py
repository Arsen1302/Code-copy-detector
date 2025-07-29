class Solution:
    def solution_1374_1(self, operations: List[str]) -> int:
        x = 0
        for o in operations:
            if '+' in o:
                x += 1
            else:
                x -= 1
        return x