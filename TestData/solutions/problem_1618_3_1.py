class Solution:
    def solution_1618_3_1(self, nums: List[int]) -> int:
        
        def solution_1618_3_2(n):
    
            sum = 0
            for digit in str(n): 
              sum += int(digit)      
            return sum

        hashmap = {}
        sumMax = -1
        for i in range(len(nums)):
            complement = solution_1618_3_2(nums[i])
            if complement in hashmap:
                sumMax = max(sumMax, nums[i] + hashmap[complement])
                if nums[i] > hashmap[complement]:
                    hashmap[complement] = nums[i]
            else:
                hashmap[complement] = nums[i]

        return sumMax