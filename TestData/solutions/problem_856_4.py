class Solution:
    def solution_856_4(self, n: int) -> List[int]:
        mid = n // 2
        if (n &amp; 1): return [num for num in range(-mid, mid + 1)]
        else: return [num for num in range(-mid, mid + 1) if num != 0]