class Solution:
    def solution_1701_2(self, nums: List[int], target: List[int]) -> int:
        return sum(map(lambda p:abs(p[1]-p[0]), zip(list(sorted([i + 10**9 * (i%2) for i in nums])), list(sorted([j + 10**9 * (j%2) for j in target])))))>>2