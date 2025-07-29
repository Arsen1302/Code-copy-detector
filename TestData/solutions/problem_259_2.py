class Solution:
    def solution_259_2(self, x: int, y: int) -> int:
        return bin(x^y).replace("0b","").count('1')