class Solution:
    def solution_918_2 (self, matrix: List[List[int]]) -> List[int]:
        return set(map(min, matrix)) &amp; set(map(max, zip(*matrix)))