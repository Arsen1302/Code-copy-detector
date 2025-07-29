class Solution:
    def solution_220_2_1(self, nums: [int], m: int) -> int:
        prefixSum = []
        curSum = 0 
        for num in nums: 
            curSum += num
            prefixSum.append(curSum)
        self.prefixSum = prefixSum   
        memo = dict()
        minMax = self.solution_220_2_3(0, m-1, memo)
        return minMax
        
    def solution_220_2_2(self, start: int, end: int) -> int: 
        res = self.prefixSum[end]
        res -= self.prefixSum[start-1] if start-1 >= 0 else 0 
        return res
    
    def solution_220_2_3(self, index: int, splits: int, memo: dict) -> int: 
        if splits == 0: 
            subarray = self.solution_220_2_2(index, len(self.prefixSum)-1)
            return subarray
        
        key = (index, splits) 
        if key in memo: 
            return memo[key]
        
        minMax = float('inf')
        maxIndex = len(self.prefixSum)-splits
        for i in range (index, maxIndex): 
            subarray = self.solution_220_2_2(index, i)
            maxLeftover = self.solution_220_2_3(i+1, splits-1, memo)
            maximum = max(subarray, maxLeftover) 
            minMax = min(minMax, maximum)
        memo[key] = minMax
        return minMax