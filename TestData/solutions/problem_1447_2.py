class Solution:
    def solution_1447_2(self, arr: List[int], k: int) -> int:
        ans = 0 
        for _ in range(k): 
            vals = []
            for i in range(_, len(arr), k): 
                if not vals or vals[-1] <= arr[i]: vals.append(arr[i])
                else: vals[bisect_right(vals, arr[i])] = arr[i]
            ans += len(vals)
        return len(arr) - ans