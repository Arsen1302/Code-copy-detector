class Solution:
    def solution_200_5(self, s, t):
        r = [0] * 26
        
        for c in s: r[ord(c) - ord('a')] -= 1
        for c in t: r[ord(c) - ord('a')] += 1
        
        for i,n in enumerate(r):
            if n > 0: return chr(i + ord('a'))