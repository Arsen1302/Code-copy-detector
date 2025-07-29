class Solution:
    # Simple query traversal approach
	# Check if previously the nums element was even or odd
	# If it was even we just need to remove it or update the ressum based on the new result being even or odd
	# If it was odd we need to add to the ressum only if the new value becomes even
    def solution_665_3(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ressum = sum([num for num in nums if not num &amp; 1])
        res = []
        for val, i in queries:
            if nums[i] &amp; 1:
                if not nums[i] + val &amp; 1:
                    ressum += nums[i] + val
            else:
                if not nums[i] + val &amp; 1:ressum += val
                else: ressum -= nums[i]
            res.append(ressum)  
            nums[i] += val
        return res