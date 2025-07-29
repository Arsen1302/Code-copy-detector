class Solution:
    def solution_989_3(self, arr: List[int], k: int) -> List[int]:
        z = sorted(arr)
        n = len(arr)
        median = (n-1)//2
        i = 0
        j = n-1
        res = []
        while len(res) != k:
            if z[j]-z[median] > z[median]-z[i] or (z[j]-z[median] == z[median]-z[i] and z[j] >= z[i]):
                res.append(z[j])
                j -= 1
            elif z[j]-z[median] < z[median]-z[i] or (z[j]-z[median] == z[median]-z[i] and z[j] < z[i]):
                res.append(z[i])
                i += 1
        return res