class Solution:
    def solution_1286_2(self, nums: List[int]) -> int:
        cnt = 0
        n  = len(nums)
        nums.sort()
        i=1
        prev = nums[0]
        while i<n:
            while i<n and nums[i]==prev:
                i+=1
            cnt = cnt + n-i
            if i<n:
                prev = nums[i]
        
        return cnt