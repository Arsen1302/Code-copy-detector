class Solution:
    def solution_1571_3(self, candidates: List[int]) -> int:
        arr = [0]*32
        for c in candidates:
            for i in range(0, 30):
                if c &amp; (1<<i) :
                    arr[i] += 1
        return max(arr)