class Solution:
    def solution_153_5_1(self, nums: List[int]) -> List[int]:
        def solution_153_5_2(nums,start,mid,end,res):
            left = start
            right = mid + 1
            result = []
            inversion_count = 0 
            while left <= mid and right <= end:
                if nums[left][1] <= nums[right][1]:
                    res[nums[left][0]] += inversion_count                   
                    result.append(nums[left])
                    left += 1
                else:
                    inversion_count+=1 
                    result.append(nums[right])
                    right += 1

            while left <= mid:
                res[nums[left][0]] += inversion_count
                result.append(nums[left])
                left += 1

            while right <= end:
                result.append(nums[right])
                right += 1 

            j = 0 
            for i in range(start,end+1):
                nums[i] = result[j]
                j+=1
    
    
        def solution_153_5_3(nums,start,end,res):
            if start<end:
                mid = (start + end)//2
                solution_153_5_3(nums,start,mid,res)
                solution_153_5_3(nums,mid+1,end,res)

                solution_153_5_2(nums,start,mid,end,res)
        
        n = len(nums)
        nums = list(enumerate(nums))
        res = [0]*n
        solution_153_5_3(nums,0,n-1,res)
        return res