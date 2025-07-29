class Solution:
    def solution_45_2(self, s: str) -> int:
        ans = [inf]*len(s) + [0] #min palindrome partition for s[i:]
        for k in reversed(range(len(s))): 
            for i, j in (k, k), (k, k+1):
                while 0 <= i and j < len(s) and s[i] == s[j]: 
                    ans[i] = min(ans[i], 1 + ans[j+1])
                    i, j = i-1, j+1
        return ans[0]-1