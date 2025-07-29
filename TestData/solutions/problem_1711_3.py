class Solution:
    def solution_1711_3(self, nums: List[int], k: int) -> int:
        seen = set()
        res = 0
        curr = 0
        for i in range(len(nums)):
            if nums[i] not in seen:
                if len(seen) < k:
                    seen.add(nums[i])
                    curr += nums[i]
                if len(seen) == k:
                    res = max(res, curr)
                    curr -= nums[i-k+1]
                    seen.remove(nums[i-k+1])
            else:
                seen = {nums[i]}
                curr = nums[i]
            
        return res