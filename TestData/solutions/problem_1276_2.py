class Solution:
    def solution_1276_2(self, s: str) -> int:
        k = 3
        if k > len(s):
            return 0
        
        letter_frequency = {}
        count, windowStart = 0, 0
        for windowEnd in range(len(s)):
            if s[windowEnd] not in letter_frequency:
                letter_frequency[s[windowEnd]] = 0
            letter_frequency[s[windowEnd]] += 1
            
            if windowEnd >= k - 1:
                if len(letter_frequency) == k:
                    count+=1
                letter_frequency[s[windowStart]] -= 1
                if letter_frequency[s[windowStart]] ==0:
                    del letter_frequency[s[windowStart]]
                windowStart += 1
        return count