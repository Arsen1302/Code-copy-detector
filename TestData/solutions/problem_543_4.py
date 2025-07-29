class Solution:
    def solution_543_4(self, S: str) -> int:
        ans = k = 0
        for i in range(len(S)): 
            k += 1 if S[i] == "(" else -1
            if S[i-1:i+1] == "()": ans += 2**k
        return ans