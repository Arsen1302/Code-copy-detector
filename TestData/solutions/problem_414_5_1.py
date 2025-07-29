class Solution:
    def solution_414_5_1(self, nums: List[int], k: int) -> bool:
        
        total = sum(nums)
        if total%k:
            return False
        partitions = [total//k]*k
        
        # Sorting was an after thought to get rid of the TLEs
        nums.sort(reverse=True)
        
        # Attempt allocating nums to the partitions, backtrack if not possible
        def solution_414_5_2(i):
            if i >= len(nums):
                return True
            for idx in range(k):
                if nums[i] <= partitions[idx]: 
                    partitions[idx] -= nums[i]
                    if solution_414_5_2(i+1):
                        return True
                    partitions[idx] += nums[i]
        
        return solution_414_5_2(0)