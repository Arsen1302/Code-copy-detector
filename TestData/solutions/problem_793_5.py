class Solution:
    def solution_793_5(self, arr: List[int]) -> List[List[int]]:
        minDif = float('+inf')
        res = []
        arr.sort()
        for i in range(1, len(arr)):
            d = arr[i] - arr[i - 1]
            if d == minDif:
                res.append([arr[i - 1], arr[i]])
            elif d < minDif:
                res = [[arr[i- 1], arr[i]]]
                minDif = d
        return res