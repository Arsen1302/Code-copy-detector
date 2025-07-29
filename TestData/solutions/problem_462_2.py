class Solution:
    def solution_462_2(self, arr: List[int]) -> int:
        S = []
        for a in arr:
            min_i, max_i = a, a
            while S and a < S[-1][1]:
                start, end = S.pop()
                min_i, max_i = min(start, min_i), max(end, max_i)
            S.append([min_i, max_i])
        return len(S)