class Solution:
    def solution_102_1_1(self, nums: List[int], k: int) -> int:                    
        n = len(nums)
        
        def solution_102_1_2(l, r, pivot):
            pivot_elem=nums[pivot]
            nums[r],nums[pivot]=nums[pivot],nums[r]
            
            index=l
            for i in range(l, r):
                if nums[i]<pivot_elem:
                    nums[i],nums[index]=nums[index],nums[i]
                    index+=1
            
            nums[index],nums[r]=nums[r],nums[index]
            return index
        
        def solution_102_1_3(l,r,kth_index):
            if l==r:
                return nums[l]
            
            pivot_index=solution_102_1_2(l,r,l)
            
            if pivot_index==kth_index:
                return nums[pivot_index]
            
            if kth_index>pivot_index:
                return solution_102_1_3(pivot_index+1, r, kth_index)
            else:
                return solution_102_1_3(l,pivot_index-1, kth_index)
        
        return solution_102_1_3(0, n - 1, n - k)