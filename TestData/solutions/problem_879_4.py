class Solution:
    def solution_879_4(self, arr):
        return map({n:r+1 for r,n in enumerate(sorted(set(arr)))}.get, arr)