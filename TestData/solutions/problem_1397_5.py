class Solution:
    def solution_1397_5(self, nums: List[int]) -> int:
        hmap=defaultdict(int)
        l=len(nums)
        for i in range(2**l):
            subset=0
            for j in range(l):
                if i&amp;(1<<j):
                    subset|=nums[j]
            hmap[subset]+=1
        return hmap[max(hmap)]