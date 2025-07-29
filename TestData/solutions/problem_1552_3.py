class Solution:
    def solution_1552_3(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        line = []
        for start, end in flowers: 
            line.append((start, +1))
            line.append((end+1, -1))
        vals = []
        prefix = 0 
        for x, y in sorted(line): 
            prefix += y
            vals.append((x, prefix))
        ans = []
        for p in persons: 
            i = bisect_right(vals, p, key=lambda x: x[0])
            if i: ans.append(vals[i-1][1])
            else: ans.append(0)
        return ans