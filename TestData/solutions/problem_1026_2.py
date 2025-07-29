class Solution:
    def solution_1026_2(self, arr: List[int]) -> int:
        cur = total = 0
        for i in range(len(arr)):
            if arr[i] &amp; 1: cur = i+1 - cur
            total += cur
        return total % 1000000007