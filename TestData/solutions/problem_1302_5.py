class Solution:
    def solution_1302_5(self, nums: List[int]) -> bool:
        prev = 0
        flag = False
        nums.append(math.inf)
        i, n = 0, len(nums) - 1
        while i < n:
            if prev < nums[i] < nums[i+1]:
                prev = nums[i]
            else:  # nums[i] or nums[i+1] should be removed
                if flag:
                    return False
                flag = True
                if nums[i+1] <= prev:  # remove nums[i+1]
                    prev = nums[i]
                    i += 1
            i += 1
        
        return True