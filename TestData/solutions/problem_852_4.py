class Solution:
    def solution_852_4(self, arr: List[int]) -> List[int]:
        m = -1
        for i in reversed(range(len(arr))):
            arr[i], m = m, max(m, arr[i])
        return arr