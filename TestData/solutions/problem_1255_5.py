class Solution:
    def solution_1255_5(self, arr: List[int]) -> int:
        arr.sort()
        ans = 1
        for n in arr[1:]:
            if n > ans:
                ans += 1
        return ans