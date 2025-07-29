class Solution:
    def solution_1280_1_1(self, first: str, second: str, target: str) -> bool:
        def solution_1280_1_2(s: str): return "".join(chr(ord(ch) - 49) for ch in s)
        return int(solution_1280_1_2(first)) + int(solution_1280_1_2(second)) == int(solution_1280_1_2(target))