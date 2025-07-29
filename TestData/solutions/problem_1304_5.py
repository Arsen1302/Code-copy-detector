class Solution:
    def solution_1304_5(self, nums: List[int]) -> int:
        vals = []
        for x in nums: 
            if not vals or vals[-1] != x: 
                vals.append(x)
                
        peaks, valleys = [], []
        for i in range(len(vals)): 
            if (-inf if i == 0 else vals[i-1]) < vals[i] > (-inf if i+1 == len(vals) else vals[i+1]): peaks.append(vals[i])
            if 0 < i < len(vals)-1 and vals[i-1] > vals[i] < vals[i+1]: valleys.append(vals[i])
        if len(peaks) == len(valleys): valleys.pop()
        return sum(peaks) - sum(valleys)