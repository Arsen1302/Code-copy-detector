class Solution:
    def solution_858_3(self, arr: List[int], start: int) -> bool:
        vis = [0]*len(arr)
        pos = [start]
        while pos:
            nextPos = []
            while pos:
                x = pos.pop()
                if arr[x] == 0: return True
                vis[x] = 1
                for y in (x-arr[x], x+arr[x]):
                    if 0 <= y < len(arr) and not vis[y]: nextPos.append(y)
            pos = nextPos
        return False