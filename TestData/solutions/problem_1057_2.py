class Solution:
    def solution_1057_2(self, arr: List[int], m: int, k: int) -> bool:
        if len(arr) < k*m: return False
        arr = ''.join([str(x) for x in arr])
        return any([ a==a[0:m]*k for a in [arr[i:i+m*k] for i in range(len(arr))] ])