class Solution:
    def solution_1325_3(self, segments: List[List[int]]) -> List[List[int]]:
        vals = []
        for start, end, color in segments: 
            vals.append((start, +color))
            vals.append((end, -color))
        
        ans = []
        prefix = prev = 0 
        for x, c in sorted(vals): 
            if prev < x and prefix: ans.append([prev, x, prefix])
            prev = x
            prefix += c 
        return ans