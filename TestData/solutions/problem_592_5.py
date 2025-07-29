class Solution:
    def solution_592_5(self, nums: List[int], k: int) -> int:
        a = max(nums)
        b = min(nums)
       
        #Since the minimum output we can get is 0 due to ranges being unable to have negative length, 

        #the ideal situation is: max(nums)-x == min(nums)-y, x and y in range [-k,k]

        #And this means: max(nums)-k <= min(nums)+k or max(nums) - min(nums) <= 2*k 
        
        #If that is the case we return 0

        if a - b <= 2*k: 
            return 0

        #If not then we get max(nums) and min(nums) as close as possible
        
        #through : (max(nums)-k) - (min(nums) + k) == max(nums) - min(nums) - 2*k

        return a - b - 2*k