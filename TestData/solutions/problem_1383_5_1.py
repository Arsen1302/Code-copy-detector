class Solution:
    def solution_1383_5_1(self, answerKey: str, k: int) -> int:
        
        def solution_1383_5_2(target): 
            """Return max consecutive target."""
            ans = cnt = ii = 0 
            for i, x in enumerate(answerKey): 
                if x == target: cnt += 1 
                while cnt > k: 
                    if answerKey[ii] == target: cnt -= 1
                    ii += 1
                ans = max(ans, i - ii + 1)
            return ans 
        
        return max(solution_1383_5_2("T"), solution_1383_5_2("F"))