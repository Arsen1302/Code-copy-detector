class Solution:
    def solution_1352_5(self, nums: List[int]) -> int:
        l,h = min(nums),max(nums) #we create these temps instead of calling min &amp; max in iteration to increase speed
        for t in range(l,0,-1): #divisor will always be smaller than low 
            if l % t == 0 and h % t == 0: return t 
        return 1 #else claus