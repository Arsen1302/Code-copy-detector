class Solution:
    def solution_580_3(self, A: List[str]) -> int:
        fn = lambda s: "".join(sorted(s[::2]) + sorted(s[1::2]))
        return len(set(fn(s) for s in A))