class Solution:
    def solution_1534_4(self, matches: List[List[int]]) -> List[List[int]]:
        counts = defaultdict(int)
        for winner, loser in matches:
            counts[winner] += 0
            counts[loser] += 1
        return [sorted(key for (key, value) in counts.items() if value == 0), sorted(key for (key, value) in counts.items() if value == 1)]