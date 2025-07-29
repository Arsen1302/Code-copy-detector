class Solution: 
    def solution_1645_5(self, s: str, shifts: List[List[int]]) -> str:
        ops = []
        for start, end, direction in shifts: 
            direction = 2*direction-1
            ops.append((start, direction))
            ops.append((end+1, -direction))
        ops.sort()
        ans = []
        prefix = ii = 0 
        for i, ch in enumerate(s): 
            while ii < len(ops) and ops[ii][0] == i: 
                prefix += ops[ii][1]
                ii += 1
            ans.append(chr((ord(ch)-97+prefix)%26+97))
        return ''.join(ans)