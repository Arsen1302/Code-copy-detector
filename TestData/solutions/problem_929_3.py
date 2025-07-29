class Solution:
    def solution_929_3(self, arr: List[int]) -> int:
        return max([a for a in arr if arr.count(a)==a], default=-1)