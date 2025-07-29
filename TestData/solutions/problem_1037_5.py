class Solution:
    def solution_1037_5(self, arr: List[int], k: int) -> int:
        curr = k
        for i in arr:
            if i<=curr:
                curr +=1
        return curr