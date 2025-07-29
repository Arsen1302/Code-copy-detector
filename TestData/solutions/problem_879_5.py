class Solution:
    def solution_879_5(self, arr: List[int]) -> List[int]:
        rank = {}
        cnt = 1
        for i in sorted(list(set(arr))):
            rank[i] = cnt
            cnt += 1
        #print(rank)
        return [rank[i] for i in arr]