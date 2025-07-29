class Solution:
    def solution_463_3(self, nums: List[int]) -> int:
        chunks = 0
        left = 0
        n = len(nums)
        smallest, largest = n, -1

        for right, num in enumerate(nums):
            smallest =  min(smallest, num)
            largest = max(largest, num)
            if left <= smallest and largest <= right:
                chunks += 1
                left = right + 1
                smallest, largest = n, -1
        
        return chunks