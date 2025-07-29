class Solution:
    def solution_306_1(self, a: str, b: str) -> int:
        if a==b:return -1
        else:return max(len(a),len(b))