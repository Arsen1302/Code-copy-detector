class Solution:
    def solution_1045_4(self, arr):
        return "111" in "".join(map(lambda x:str(x%2), arr))