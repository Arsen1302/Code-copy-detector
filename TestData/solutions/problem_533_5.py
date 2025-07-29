class Solution:
    def solution_533_5(self, arr: List[int]) -> int:
        longest = 0
        left = 0
        rise_seen = False
        fall_seen = False
        for right in range(1, len(arr)):
            a, b = arr[right - 1], arr[right]
            if a < b:
                if fall_seen:
                    left = right - 1
                rise_seen = True
                fall_seen = False
            elif a == b:
                rise_seen = False
                fall_seen = False
                left = right
            else:
                fall_seen = True
                if rise_seen:
                    longest = max(longest, right - left + 1)
        return longest