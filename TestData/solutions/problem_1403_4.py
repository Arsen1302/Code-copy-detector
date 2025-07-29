class Solution:
    # Use frequency counter to filter the array.
    
    def solution_1403_4(self, arr: List[str], k: int) -> str:
        freq = Counter(arr)
        return [s for s in arr if freq[s] == 1][k-1] if k-1 < len([s for s in arr if freq[s] == 1]) else ""

    # O(n) time : O(n) space
    def solution_1403_4(self, arr: List[str], k: int) -> str:
        freq = Counter(arr)
        distinct = [s for s in arr if freq[s] == 1]
        return distinct[k-1] if k-1 < len(distinct) else ""