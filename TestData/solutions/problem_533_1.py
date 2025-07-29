class Solution:
    def solution_533_1(self, arr: List[int]) -> int:
        increasing = False
        increased = False
        mx = -math.inf
        curr = -math.inf
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                if increasing:
                    curr += 1
                    increased = True
                else:
                    mx = max(curr, mx)
                    curr = 2
                    increased = True
                    increasing = True
            elif arr[i] < arr[i-1]:
                if increasing:
                    increasing = False
                curr += 1
            else:
                if increased and not increasing:
                    mx = max(mx, curr)
                curr = -math.inf
                increased = False
                increasing = False
        if not increasing and increased:
            mx = max(mx, curr)
        return 0 if mx == -math.inf else mx