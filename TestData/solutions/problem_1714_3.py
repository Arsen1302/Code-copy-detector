class Solution:
    def solution_1714_3(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        j=n-1
        s=set()
        nums.sort()
        while i<=j:
            s.add((nums[i]+nums[j])/2)
            i+=1
            j-=1
        return len(s)