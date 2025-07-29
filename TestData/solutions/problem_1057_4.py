class Solution:
    def solution_1057_4(self, arr: List[int], m: int, k: int) -> bool:
        ans = 0
        memo = [1]*len(arr) # repetition of pattern ending at i
        for i in range(len(arr)): 
            if arr[i+1-m:i+1] == arr[i+1-2*m:i+1-m]: memo[i] = 1 + memo[i-m]
            if memo[i] == k: return True
        return False