class Solution:
    def solution_393_3(self, num: int) -> int:
        nums = [int(x) for x in str(num)]
        
        _max = -1
        _max_idx = 0
        last_max_idx, last_min_idx = 0, 0
        
        for idx in range(len(nums) - 1, -1, -1):
            if nums[idx] > _max:
                _max = nums[idx]
                _max_idx = idx
            elif nums[idx] < _max:
                last_min_idx = idx
                last_max_idx = _max_idx
        
        nums[last_max_idx], nums[last_min_idx] = nums[last_min_idx], nums[last_max_idx]
        
        return int(''.join([str(num) for num in nums]))