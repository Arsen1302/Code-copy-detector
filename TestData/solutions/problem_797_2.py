class Solution:
    def solution_797_2(self, arr: List[int]) -> bool:
        from collections import Counter
        c = Counter(arr)
        return len(c) == len({c[x] for x in c})