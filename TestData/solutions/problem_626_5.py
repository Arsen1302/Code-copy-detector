class Solution:
    def solution_626_5(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        moves = 0
        prev = nums[0]
        for i in range(1, n):
            if nums[i] <= prev:
                moves = moves + prev +1 - nums[i]
                nums[i] = prev +1          
            prev = nums[i]
        return moves
            
Runtime: 1151 ms, faster than 48.92% of Python3 online submissions for Minimum Increment to Make Array Unique.
Memory Usage: 28.3 MB, less than 50.69% of Python3 online submissions for Minimum Increment to Make Array Unique.