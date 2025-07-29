class Solution:
    def solution_220_3_1(self, nums: [int], m: int) -> int:
        prefixSum = []
        curSum = 0 
        for num in nums: 
            curSum += num
            prefixSum.append(curSum)
        self.prefixSum = prefixSum   
        memo = [[-1] * m for i in range (len(nums))]
        minMax = self.solution_220_3_3(0, m-1, memo)
        return minMax
        
    def solution_220_3_2(self, start: int, end: int) -> int: 
        res = self.prefixSum[end]
        res -= self.prefixSum[start-1] if start-1 >= 0 else 0 
        return res
    
    def solution_220_3_3(self, index: int, splits: int, memo: [[int]]) -> int: 
        if splits == 0: 
            subarray = self.solution_220_3_2(index, len(self.prefixSum)-1)
            return subarray
        
        if memo[index][splits] != -1: 
            return memo[index][splits]
        
        minMax = float('inf')
        low = index
        high = len(self.prefixSum)-splits-1
        while low <= high: 
            mid = low + (high-low) // 2
            subarray = self.solution_220_3_2(index, mid)
            maxLeftover = self.solution_220_3_3(mid+1, splits-1, memo)
            minMax = min(minMax, max(subarray, maxLeftover))
            if subarray < maxLeftover: 
                low = mid+1
            elif subarray > maxLeftover: 
                high = mid-1
            else: 
                break 
        memo[index][splits] = minMax
        return minMax