class Solution:
    def solution_929_1(self, arr: List[int]) -> int:
        
        charMap = {}
        
        for i in arr:
            charMap[i] = 1 + charMap.get(i, 0)
            
        res = []
        
        for i in charMap:
            if charMap[i] == i:
                res.append(i)
                
        res = sorted(res)    
        
        if len(res) > 0:
            return res[-1]
            
        return -1