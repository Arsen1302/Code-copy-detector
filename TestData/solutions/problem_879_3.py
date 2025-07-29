class Solution:
    def solution_879_3(self, arr):
        ranks = {num:rank+1 for rank, num in enumerate(sorted(set(arr)))}
        return [ranks[num] for num in arr]