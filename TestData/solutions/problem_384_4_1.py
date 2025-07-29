class Solution:
    def solution_384_4_1(self, arr: List[int], k: int, x: int) -> List[int]:
        # find the closest number
        right = self.solution_384_4_2(arr, x)
        left = right - 1
        
        # get the pointers array
        for _ in range(k):
            if self.solution_384_4_3(arr, left, right, x) == right:
                right += 1
            else:
                left -= 1
        left = 0 if right - k < 0 else right - k
        print(left, right)
        return arr[left:] if left == right else arr[left:right]
            
        
        
    def solution_384_4_2(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        
        return self.solution_384_4_3(nums, left, right, target)
    
    def solution_384_4_3(self, nums, left, right, target):
        if left < 0:
            return right
        if right > len(nums) - 1:
            return left
        return left if abs(nums[left] - target) <= abs(nums[right] - target) else right