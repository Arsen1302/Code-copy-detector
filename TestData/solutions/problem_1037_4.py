class Solution:
    def solution_1037_4(self, arr: List[int], k: int) -> int:
        n_missing = lambda i: arr[i]-i-1
        left, right = 0, len(arr)
        while left < right:
            mid = left+(right-left)//2
            if n_missing(mid) >= k:
                right = mid
            else:
                left = mid+1
        # if more n_missing at the last index than k
        if left < len(arr):
            return arr[left]-(n_missing(left)-k+1)
        # if fewer n_missing at the last index than k
        return arr[len(arr)-1]+(k-n_missing(len(arr)-1))