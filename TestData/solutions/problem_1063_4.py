class Solution:
    def solution_1063_4(self, arr: List[int]) -> int:

        left, right = 0, len(arr) - 1
        while left < len(arr) - 1 and arr[left] <= arr[left + 1]:
            left += 1
        if left == right: return 0

        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1

        res = inf
        for i in range(left + 1):
            if arr[-1] < arr[i]:
                res = min(res, len(arr) - i - 1)
                continue

            lo, hi = right, len(arr) - 1
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if arr[mid] >= arr[i]:
                    hi = mid
                else:
                    lo = mid + 1
            res = min(res, hi - i - 1)

        for i in range(right, len(arr)):
            if arr[0] > arr[i]:
                res = min(res, right)
                continue

            lo, hi = 0, left
            while lo < hi:
                mid = lo + (hi - lo + 1) // 2
                if arr[mid] <= arr[i]:
                    lo = mid
                else:
                    hi = mid - 1
            res = min(res, i - lo - 1)

        return res