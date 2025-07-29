class Solution:
    def solution_737_4(self, tiles: str) -> int:
         return len(set(sum([list(itertools.permutations(tiles, i)) for i in range(1, len(tiles) + 1)], [])))