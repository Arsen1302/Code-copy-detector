class Solution:
    def solution_1247_3(self, costs: List[int], coins: int) -> int:
        return len([i for i in itertools.accumulate(sorted(costs)) if i <= coins])