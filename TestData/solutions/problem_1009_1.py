class Solution:
    def solution_1009_1(self, arr: List[int]) -> bool:
        arr.sort()
        return len(set(arr[i-1] - arr[i] for i in range(1, len(arr)))) == 1