class Solution:
    def solution_604_5(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            swapped= False
            for j in range(n-i-1):
                if nums[j]%2==0 and j%2!=0  :
                    for k in range(j+1,n):
                        if k%2==0 and nums[k]%2!=0:
                            x = nums[j]
                            nums[j]= nums[k]
                            nums[k]= x
                            swapped= True
                            break;
                elif nums[j]%2!=0 and j%2==0  :
                    for k in range(j+1,n):
                        if k%2!=0 and nums[k]%2==0:
                            x = nums[j]
                            nums[j]= nums[k]
                            nums[k]= x
                            swapped= True
                            break; 
            if not swapped :
                return nums
        return nums