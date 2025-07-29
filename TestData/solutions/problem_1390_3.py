class Solution:
    def solution_1390_3(self, grid: List[List[int]], x: int) -> int:
        
        # flatten the numbers
        nums = []
        for row in grid:
            for num in row:
                nums.append(num)
        
        # sort and find the median
        nums.sort()
        n = len(nums)
        median = nums[n//2]
        
        # calculate the number of operations required
        operations = 0
        for num in nums:
            diff = abs(median-num)
            if diff%x !=0:
                return -1
            operations += diff//x
        
        return operations