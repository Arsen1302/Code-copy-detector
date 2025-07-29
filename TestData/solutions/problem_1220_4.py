class Solution:
    def solution_1220_4(self, nums: List[int], k: int) -> int:
        length = len(nums)
        maximumPossibleScore = nums[k]
        minimum = nums[k]
        left = k
        right = k
        
        while left > 0 or right < length - 1:
            if left > 0 and right < length - 1:
                if nums[left - 1] > nums[right + 1]:
                    left -= 1
                    minimum = min(minimum, nums[left])
                else:
                    right += 1
                    minimum = min(minimum, nums[right])
            
            elif left > 0:
                left -= 1
                minimum = min(minimum, nums[left])
            
            else:
                right += 1
                minimum = min(minimum, nums[right])
            
            score = minimum*(right-left+1)
            maximumPossibleScore = max(maximumPossibleScore, score)
        
        return maximumPossibleScore