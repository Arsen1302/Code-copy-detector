class Solution:
    def solution_1043_5(self, nums: List[int], target: int) -> int:
        
        moddict = {}
        moddict[0] = 0
        
        res = 0  # value to be returned
        
        cnt = 1
        s = 0 
        
        for num in nums:
            s += num
            if s-target in moddict:
                res += 1
                moddict = {}
            moddict[s] = cnt
            
            cnt += 1
        return res