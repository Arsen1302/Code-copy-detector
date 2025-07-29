class Solution:
    def solution_1714_1(self, nums: List[int]) -> int:
        av=[]
        nums.sort()
        while nums:
            av.append((nums[-1]+nums[0])/2)
            nums.pop(-1)
            nums.pop(0)
        return len(set(av))