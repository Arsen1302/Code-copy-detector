class Solution:
    def solution_445_3(self, letters: List[str], target: str) -> str:
        low, high = 0, len(letters) - 1
        while low < high:
            mid = (low+high) // 2
            if letters[mid] <= target:
                low = mid + 1
            else:
                high = mid
        return letters[low] if letters[low] > target else letters[0]