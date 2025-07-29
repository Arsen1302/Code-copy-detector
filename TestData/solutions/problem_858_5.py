class Solution:
    def solution_858_5(self, arr: List[int], start: int) -> bool:
        stack = [start]
        arr[start] *= -1 # mark "visited"
        while stack: 
            i = stack.pop()
            if arr[i] == 0: return True 
            for ii in i - arr[i], i + arr[i]: 
                if 0 <= ii < len(arr) and arr[ii] >= 0: 
                    stack.append(ii)
                    arr[ii] *= -1 
        return False