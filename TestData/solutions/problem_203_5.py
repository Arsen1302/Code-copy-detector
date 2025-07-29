class Solution:
    def solution_203_5(self, s: str, t: str) -> bool:
        it = iter(t)
        return all(ch in it for ch in s)