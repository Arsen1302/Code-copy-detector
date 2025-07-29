class Solution:
    def solution_852_1(self, arr: List[int]) -> List[int]:
        mx = arr[-1]
        arr[-1] = -1
        for i in range(len(arr) - 2, -1, -1):
            temp = arr[i]
            arr[i] = mx
            if mx < temp: mx = temp
        return arr