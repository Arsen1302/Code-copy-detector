class Solution:
def solution_1304_1(self, nums: List[int]) -> int:
    
    ma=0
    mi=0
    for num in nums:
        ma=max(ma,num-mi)
        mi=min(mi,num-ma)
        
    return ma