class Solution:
    def solution_1066_3_1(self, nums1: List[int], nums2: List[int]) -> int:      
        nums1.sort()
        nums2.sort()
        
        def solution_1066_3_2(target, left, right, nums):
            while left < right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    right = mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            
            return left
        
        def solution_1066_3_3(target, left, right, nums):
            while left < right:
                mid = left + (right - left) // 2
                
                if nums[mid] == target:
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            
            return left
            
    
        def solution_1066_3_4(n, nums, memo):
            if n in memo:
                return memo[n]
            
            result = 0
            
            for i in range(len(nums)):
                if n % nums[i] != 0:
                    continue
                    
                target = n // nums[i]
                
                # find total number of target in nums[i+1:]
                lower = solution_1066_3_2(target, i+1, len(nums), nums)
                higher = solution_1066_3_3(target, i+1, len(nums), nums)
                
                result += (higher - lower)
            
            memo[n] = result
            return result
        
        result = 0
        
        memo1 = {}
        for n in nums1:
            result += solution_1066_3_4(n*n, nums2, memo1)
        
        memo2 = {}
        for n in nums2:
            result += solution_1066_3_4(n*n, nums1, memo2)
        
        return result