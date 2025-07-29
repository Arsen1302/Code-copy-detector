class Solution:
    def solution_889_3(self, arr: List[int], k: int, threshold: int) -> int:
        ans = sm = 0 
        for i, x in enumerate(arr): 
            sm += x
            if i >= k: sm -= arr[i-k]
            if i+1 >= k and sm >= k*threshold: ans += 1
        return ans