class Solution:
    def solution_1613_3(self, nums: List[int], t: int) -> int:
        n = len(nums)
        if t / n >= max(nums):
            return -1
        
        left = list(range(n))
        right = list(range(n))

        # leftmost boundary for the subarray for each index
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                left[i] = left[stack.pop()]
            stack.append(i)
            
        # rightmost boundary for the subarray for each index
        stack = []
        for i in reversed(range(n)):
            while stack and nums[stack[-1]] >= nums[i]:
                right[i] = right[stack.pop()]
            stack.append(i)

        # get size of subarray and if eligible then output
        for i in range(n):
            size = right[i] - left[i] + 1
            if nums[i] > t / size:
                return size
        
        return -1