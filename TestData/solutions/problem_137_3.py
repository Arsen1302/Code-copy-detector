class Solution:
    def solution_137_3(self, n: int) -> int:
        low,high = 1, n
        while low<=high:
            mid=(low+high)//2
            isBad = isBadVersion(mid)
            if(isBad):
                high = mid-1
            else:
                low = mid+1
        return low