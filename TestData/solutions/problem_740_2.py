class Solution:
    def solution_740_2(self, arr: List[int]) -> None:
        cnt = arr.count(0)

        for i in reversed(range(len(arr))):
            if i + cnt < len(arr): arr[i + cnt] = arr[i]  # copy the number over to correct position
            if arr[i] == 0:
                cnt -= 1
                if i + cnt < len(arr): arr[i + cnt] = arr[i]  # copy again if the number is 0