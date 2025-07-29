class Solution:
        def solution_330_3(self, s):
            return " ".join([x[::-1] for x in s.split()])