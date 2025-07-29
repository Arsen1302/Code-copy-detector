class Solution:
    def solution_1444_3(self, words):
        return next((word for word in words if word==word[::-1]), "")