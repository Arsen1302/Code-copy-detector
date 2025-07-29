class Solution:
    def solution_1374_5(self, operations: List[str]) -> int:
        x = 0
        for i in range(len(operations)):
            if operations[i] == "++X" or operations[i] == "X++": x += 1 
            else: x -=1
        return x