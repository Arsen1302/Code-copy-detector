class Solution:
    def solution_1444_2_1(self, words):
        for word in words:
            if self.solution_1444_2_2(word): return word
        return ""
    
    def solution_1444_2_2(self, word):
        l, r = 0, len(word)-1
        while l < r:
            if word[l] != word[r]: return False
            l += 1
            r -= 1
        return True