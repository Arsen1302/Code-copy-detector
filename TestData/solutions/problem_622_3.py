class Solution:
    def solution_622_3(self, arr: List[int]) -> bool:
        max_num = max(arr)
        # Edge cases --> if the slope of the mountain is strictly increasing/decreasing
        if max_num == arr[len(arr) - 1] or max_num == arr[0]:
            return False
        max_found = False
        for i in range(len(arr) - 1):
            # We initially want the mountain to be increasing but
            # once we find the max number, we want the mountain to decrease
            if arr[i] == max_num:
                max_found = True
            if max_found and arr[i] <= arr[i + 1]:
                return False
            elif not max_found and arr[i] >= arr[i + 1]:
                return False
        return True