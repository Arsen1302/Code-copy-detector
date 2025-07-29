class Solution:
    def solution_785_1(self, distance: List[int], start: int, destination: int) -> int:
        a, b = min(start, destination), max(start, destination)
        return min(sum(distance[a:b]), sum(distance) - sum(distance[a:b]))