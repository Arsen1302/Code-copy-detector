class Solution:
def solution_604_1(self, nums: List[int]) -> List[int]:
    
    odd,even = [],[]
    for n in nums:
        if n%2: odd.append(n)
        else: even.append(n)
    
    o,e = 0,0
    for i in range(len(nums)):
        if i%2==0:
            nums[i]=even[e]
            e+=1
        else:
            nums[i]=odd[o]
            o+=1
    
    return nums