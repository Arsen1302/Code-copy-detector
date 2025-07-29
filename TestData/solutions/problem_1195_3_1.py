class Solution:
    def solution_1195_3_1(self, nums: List[int], maxOperations: int) -> int:
        # the maximum size increases the minimum number of bags decreases so we can binary search the maximum size
        def solution_1195_3_2(penalty):
            
            split = 0
            
            for i in nums:
                split+=(i-1)//penalty
            
            if split<=maxOperations:
                return True
            else:
                return False
            
        # if we know the maximum size of a bag what is the minimum number of bags you can make
        low = 1
        heigh = max(nums)
        
        while low<heigh:
            mid = (low+heigh)//2
            
            if solution_1195_3_2(mid):
                heigh = mid
            
            else:
                low = mid+1
                
        return low