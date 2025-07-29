class Solution:
    def solution_858_1(self, arr: List[int], i: int) -> bool:
        if i < 0 or i >= len(arr) or arr[i] < 0: return False
        arr[i] *= -1 # Mark visited
        return arr[i] == 0 or self.solution_858_1(arr, i - arr[i]) or self.solution_858_1(arr, i + arr[i])