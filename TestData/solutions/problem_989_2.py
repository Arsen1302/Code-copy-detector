class Solution:
    def solution_989_2(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        median = arr[(n - 1) // 2]
        res = []
        left, right = 0, n - 1

        for _ in range(k):
            if median - arr[left] > arr[right] - median:
                res.append(arr[left])
                left += 1
            else:
                res.append(arr[right])
                right -= 1
        
        return res