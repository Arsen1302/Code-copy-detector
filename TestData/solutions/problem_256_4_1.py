class Solution:
    def solution_256_4_1(self, nums: List[int]) -> bool:
        def solution_256_4_2(nums, cur_index, is_positive):
            direction = nums[cur_index] >= 0
            if direction != is_positive:
                return -1
            
            next_index = (cur_index+nums[cur_index])%len(nums)
            if next_index < 0:
                next_index = len(nums) - next_index 
                
            if next_index == cur_index:
                next_index = -1
                
            return next_index
        
        for index in range(len(nums)):
            is_positive = nums[index] >= 0
            fast, slow, = index, index
            while True:
                slow = solution_256_4_2(nums, slow, is_positive)
                fast = solution_256_4_2(nums, fast, is_positive)
                
                if fast != -1:
                    fast = solution_256_4_2(nums, fast, is_positive)
                if slow == -1 or fast == -1:
                    break
                if slow == fast:
                    return True
        return False