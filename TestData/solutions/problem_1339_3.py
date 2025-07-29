class Solution:
    def solution_1339_3(self, s, words):
        return s in accumulate(words)