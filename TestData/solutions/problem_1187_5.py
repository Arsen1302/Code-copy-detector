class Solution:
    def solution_1187_5(self, s: str) -> int:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]: c = s[l]  # find the same char
            else: break
                
            while l < r and s[l] == c: # exhaust left side
                l += 1
                
            while l < r and s[r] == c: # exhaust right side
                r -= 1
                
            if s[r] == c:              # if pattern like 'aa' is happening, return 0
                return 0
                
        return r - l + 1