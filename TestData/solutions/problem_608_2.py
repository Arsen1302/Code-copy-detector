class Solution:
    def solution_608_2(self, s: str) -> int:
        n = len(s)
        zero, one = [0] * n, [0] * n
        prefix = suffix = 0
        for i in range(n):
            if s[i] == '1':
                prefix += 1
            zero[i] = prefix       # flip '1' to '0'
            if s[n-1-i] == '0':
                suffix += 1
            one[n-1-i] = suffix    # flip '0' to '1' (from right to left)
            
        ans = sys.maxsize
        for i in range(n-1):
            ans = min(ans, zero[i] + one[i+1])  # `i` and its left are all '0', and '1's are on its right
        else:    
            ans = min(ans, zero[n-1], one[0])   # zero[n-1] -> all zeros, one[0] -> all ones
        return ans