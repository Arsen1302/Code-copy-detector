class Solution:
    def solution_1453_3(self, n: int, startPos: List[int], s: str) -> List[int]:
        ans = []
        for k in range(len(s)): 
            i, j = startPos
            val = 0 
            for kk in range(k, len(s)): 
                if s[kk] == 'L': j -= 1
                elif s[kk] == 'R': j += 1
                elif s[kk] == 'U': i -= 1
                else: i += 1
                if 0 <= i < n and 0 <= j < n: val += 1
                else: break 
            ans.append(val)
        return ans