class Solution:
    def solution_722_4_1(self, arr: List[int], K: int) -> int:
        length = len(arr)
        
        @cache
        def solution_722_4_2(i):
            if i >= length: return 0
            res = 0
            for count, k in enumerate(range(i, min(i+K, length)),1):
                temp = max(arr[i:k+1])*(count) + solution_722_4_2(k+1)
                res = max(res, temp)
            return res
        
        return solution_722_4_2(0)