class Solution:
    def solution_533_2(self, arr: List[int]) -> int:
        len_mountain = slope = 0
        start = -1
        arr.append(arr[-1])    # to trigger len_mountain check in the loop
        for i, (a, b) in enumerate(zip(arr, arr[1:])):
            if b > a:
                if slope < 1:
                    if slope == -1 and start > -1:
                        len_mountain = max(len_mountain, i + 1 - start)
                    start = i
                    slope = 1
            elif b < a:
                if slope == 1:
                    slope = -1
            else:
                if slope == -1:
                    if start > -1:
                        len_mountain = max(len_mountain, i + 1 - start)
                slope = 0
                start = -1
        return len_mountain