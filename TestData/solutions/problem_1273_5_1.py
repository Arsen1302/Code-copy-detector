class Solution:
    def solution_1273_5_1(self, arr, m):
        sum = 0
        for i,a in enumerate(arr):
            if(math.ceil(a/m)==math.floor(a/m) or i==len(arr)-1):
                sum += a/m
            else:
                sum += math.ceil(a/m)
        return sum
        
    
    def solution_1273_5_2(self, dist: List[int], hour: float) -> int:
        l,r = 1, 10000000
        ok = False
        while l<=r:
            mid = (l+r)//2
            if(self.solution_1273_5_1(dist, mid)<=hour):
                ok = True
                r = mid-1
            else:
                l = mid+1
        return l if ok else -1