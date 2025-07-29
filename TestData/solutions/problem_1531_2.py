class Solution:
    def solution_1531_2(self, s: str) -> int:
        prefix = []
        one = zero = 0
        for c in s:                                # find number of 0 or 1 before index `i`
            prefix.append([zero, one])
            if c == '1':
                one += 1
            else:
                zero += 1    
        suffix = []        
        one = zero = 0
        for c in s[::-1]:                          # find number of 0 or 1 after index `i`
            suffix.append([zero, one])
            if c == '1':
                one += 1
            else:
                zero += 1    
        suffix = suffix[::-1]                      # reverse since we trace from right to left 
        ans = 0
        for i, c in enumerate(s):                  # for c=='1' number of combination is prefix[i][0] * suffix[i][0] ([0 before index `i`] * [0 after index `i`])
            if c == '1':
                ans += prefix[i][0] * suffix[i][0]
            else:    
                ans += prefix[i][1] * suffix[i][1]
        return ans