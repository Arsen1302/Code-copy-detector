class Solution:
    def solution_530_4(self, S: str) -> List[int]:
        for i in range(1, min(11, len(S))): # 2**31 limit 
            if S[0] == "0" and i > 1: break 
            for j in range(i+1, min(i+11, len(S))): # 2**31 limit 
                if S[i] == "0" and j-i > 1: break 
                x, y = int(S[:i]), int(S[i:j])
                ans = [x, y]
                while j < len(S):
                    x, y = y, x+y
                    if y <= 2**31 and S[j:j+len(str(y))] == str(y): 
                        ans.append(y)
                        j += len(str(y))
                    else: break 
                else: 
                    if len(ans) > 2: return ans # no break encountered 
        return []