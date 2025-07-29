class Solution:
    def solution_1272_3(self, s: str) -> bool:
        ones = zeros = 0 
        for i in range(len(s)): 
            if i == 0 or s[i-1] != s[i]: cnt = 0 
            cnt += 1
            if s[i] == "0": zeros = max(zeros, cnt)
            else: ones = max(ones, cnt)
        return ones > zeros