class Solution:
    def solution_1571_2(self, candidates: List[int]) -> int:
		s = [0 for _ in range(30)]
        for c in candidates:
            b = bin(c)[2:][::-1]
            for i, d in enumerate(b):
                if d == '1':
                    s[i] += 1
        return max(s)