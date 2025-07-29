class Solution:
    def solution_1444_1(self, words):
        for word in words:
            if word == word[::-1]: return word
        return ""