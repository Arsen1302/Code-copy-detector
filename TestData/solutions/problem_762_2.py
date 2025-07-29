class Solution:
    def solution_762_2(self, arr: List[int]) -> int:
        ans = 0
        while len(arr) > 1: 
            i = arr.index(min(arr))
            ans += arr.pop(i)*min(arr[max(0,i-1):i+1])
        return ans