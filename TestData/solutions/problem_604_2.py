class Solution:
def solution_604_2(self, nums: List[int]) -> List[int]:
    
    e = 0                            #even_index
    o = 1                            #odd_index
    
    while e<len(nums) and o<len(nums):
        if nums[e]%2==0:
            e+=2
        else:
            if nums[o]%2!=0:
                o+=2
            else:
                nums[e],nums[o] = nums[o],nums[e]
                e+=2
                o+=2
                            
    return num