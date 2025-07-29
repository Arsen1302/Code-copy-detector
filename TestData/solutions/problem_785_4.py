class Solution:
    def solution_785_4(self, distance: List[int], start: int, destination: int) -> int:
        ans = 0
        i = start
        while i != destination: 
            ans += distance[i]
            i = (i+1) % len(distance)
        return min(ans, sum(distance) - ans)