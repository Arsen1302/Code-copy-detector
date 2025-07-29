class Solution:
    """
    Time:   O(n^2)
    Memory: O(n)
    """

    def solution_1625_3_1(self, grid: List[List[int]]) -> int:
        mp = defaultdict(int)

        for col in zip(*grid):
            mp[self.solution_1625_3_2(col)] += 1

        return sum(mp[self.solution_1625_3_2(row)] for row in grid)

    @staticmethod
    def solution_1625_3_2(nums: Generator) -> str:
        return ','.join(map(str, nums))