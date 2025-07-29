class Solution:
    def solution_1037_1(self, arr: List[int], k: int) -> int:
        ss, x = set(arr), 1
        while True: 
            if x not in ss: k -= 1
            if not k: return x
            x += 1