class Solution:
    def solution_1198_5_1(self, groups: List[List[int]], nums: List[int]) -> bool:
        pos = 0
        
        for group in groups:
            pos = self.solution_1198_5_2(nums, group, pos)
            
            if pos == -1:
                return False
            
            pos += len(group)
            
        return True
    
    # start: starting position of the next solution_1198_5_2 to check(they have to be in the same order)
    def solution_1198_5_2(self, text, pattern, start):
        lps = self.solution_1198_5_3(pattern)
        i, j = start, 0
        
        while i < len(text):
            if text[i] == pattern[j]:
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]

            if j == len(pattern):
                return i - len(pattern)

        return -1
                
    def solution_1198_5_3(self, s):
        lps = [0] * len(s)  # first lps val will always be one
        prev_lps, i = 0, 1

        while i < len(s):
            if s[i] == s[prev_lps]:
                lps[i] = prev_lps + 1
                prev_lps, i = prev_lps + 1, i + 1
            else:
                if prev_lps == 0:
                    lps[i] = 0
                    i += 1
                else:
                    prev_lps = lps[prev_lps - 1]

        return lps