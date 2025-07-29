class Solution:
    def solution_929_4(self, arr: List[int]) -> int:
        dct = {}
        for i in arr:
            dct[i] = dct.get(i, 0) + 1
        return max([key for key, value in dct.items() if key == value], default=-1)