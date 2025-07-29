class Solution:
    def solution_200_3(self, s: str, t: str) -> str:
        return list((Counter(t) - Counter(s)).keys())[0]