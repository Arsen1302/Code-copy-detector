class Solution:
    def solution_1676_3(self, nums: List[int]) -> int:
        mx = max(nums)
        return max(map(len, ''.join(map(lambda y: ('0', '1')[mx == y], nums)).split('0')))