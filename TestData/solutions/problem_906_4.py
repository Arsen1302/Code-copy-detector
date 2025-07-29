class Solution:
    def solution_906_4(self, votes: List[str]) -> str:
        counters = [Counter(v) for v in zip(*votes)]
        return ''.join(sorted(votes[0], key=lambda x:(*(-c[x] for c in counters), x)))