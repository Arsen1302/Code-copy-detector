class Solution:
    def solution_1057_5_1(self, start, end, pattern, arr, m):
        for sub_index in range(start, end + 1, m):
            if arr[sub_index:sub_index + m] != pattern:
                return False
        return True
    
    def solution_1057_5_2(self, arr: List[int], m: int, k: int) -> bool:
        window_start = 0
        window_end = m * k - 1
        length = len(arr)
        solution_1057_5_1 = False
        while window_end < length:
            pattern = arr[window_start:window_start + m]
            solution_1057_5_1 = self.solution_1057_5_1(window_start, window_end, pattern, arr, m)
            if solution_1057_5_1:
                break
            window_end += 1
            window_start += 1
        
        return solution_1057_5_1