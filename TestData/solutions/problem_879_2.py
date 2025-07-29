class Solution:
    def solution_879_2(self, arr):
        ranks = {}
        for rank, num in enumerate(sorted(set(arr))):
            ranks[num] = rank+1
        return [ranks[num] for num in arr]