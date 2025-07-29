class Solution:
    def solution_791_4(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if n == 0: return 0
        summ,gmax,cmax,gmin,cmin = arr[0],arr[0],arr[0],arr[0],arr[0]
        for i in range(1,n):
            summ += arr[i]
            cmax = max(arr[i],cmax+arr[i])
            gmax = max(cmax,gmax)
            cmin = min(arr[i],cmin+arr[i])
            gmin = min(cmin,gmin)
        if k == 1: return gmax
        opt1 = gmax + max(0,summ*(k-1))
        opt2 = summ - gmin + max(0,summ*(k-2))
        return max(opt1,opt2) % 1000000007