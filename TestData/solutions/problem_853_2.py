class Solution:
    def solution_853_2(self, arr: List[int], target: int) -> int:
        arr.sort()
        length = len(arr)
        
        for x in range(length):
            sol = round(target / length)
            if arr[x] >= sol:
                return sol
            target -= arr[x]
            length -= 1
        
        return arr[-1]