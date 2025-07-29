class Solution:
    def solution_1465_2(self, nums: List[int]) -> int:
        ones = nums.count(1)
        n = len(nums)
        res = ones
        start = 0
        end = ones-1
        zeroesInWindow = sum(num==0 for num in nums[start:end+1])
        
        while start < n:
            # print(start, end , zeroesInWindow)
            res = min(res, zeroesInWindow)
            if nums[start] == 0: zeroesInWindow -= 1 
            start += 1
            end += 1
            if nums[end%n] == 0: zeroesInWindow += 1
                
        return res