class Solution:
    def solution_992_4(self, arr, target):
        left, total, res, p = 0, 0, float("inf"), [float("inf")]

        for right in range(len(arr)):
            total += arr[right]

            while total > target:
                total -= arr[left]
                left += 1

            if total == target:
                res = min(res,p[left] + right - left + 1)
                p += [min(p[-1],right-left+1)]
            else:
                p += [p[-1]]

        return res if res != float("inf") else -1