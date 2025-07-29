class Solution:
    def solution_659_1(self, arr: List[int]) -> int:
        cur, mx, t = 1, 1, None
        for i in range(1, len(arr)):
            # Start of subarray
            if t == None:
                if arr[i] != arr[i-1]: 
                    cur = 2
                    t = arr[i] > arr[i-1]
            # Valid element in subarray, continue cur subarray
            elif (t and arr[i] < arr[i-1]) or (not t and arr[i] > arr[i-1]):
                cur += 1; t = not t
            # Invalid element in subarray, start new subarray
            else:
                if arr[i] == arr[i-1]: t = None
                mx = max(mx, cur)
                cur = 2
        
        return max(mx, cur)