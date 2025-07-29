class Solution:
    def solution_238_2_1(self, intervals: list[list[int]]) -> list[int]:
        tmp, ans = sorted(intervals), []
        indices = {tuple(j): i for i, j in enumerate(intervals)}
        for i in intervals:
            res = Solution().solution_238_2_2(tmp, i[1]) or ()
            ans.append(indices.get(tuple(res), -1))
        return ans

    def solution_238_2_2(self, arr, target):
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            element = arr[mid][0]
            if element < target:
                l = mid + 1
            elif element > target:
                r = mid - 1
            else:
                return arr[mid]
        return None if l >= len(arr) else arr[l]