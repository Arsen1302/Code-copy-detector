class Solution:
    def solution_1403_1(self, arr: List[str], k: int) -> str:
        freq = Counter(arr)
        for x in arr: 
            if freq[x] == 1: k -= 1
            if k == 0: return x
        return ""