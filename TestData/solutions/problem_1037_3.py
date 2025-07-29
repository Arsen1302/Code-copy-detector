class Solution:
    def solution_1037_3(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr)
        while left < right:
            mid = left+(right-left)//2
            n_missing = arr[mid]-mid-1
            if n_missing >= k:
                right = mid
            else:
                left = mid+1
		# if more n_missing at the last index than k
        if left < len(arr):
            n_missing = arr[left]-left
            return arr[left]-(n_missing-k)
		 # if fewer n_missing at the last index than k
        return arr[-1]+(k-arr[-1]+len(arr))