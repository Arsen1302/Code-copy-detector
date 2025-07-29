class Solution:
    def solution_906_1(self, votes: List[str]) -> str:
        teamVotes = collections.defaultdict(lambda: [0] * 26)
        for vote in votes:
            for pos, team in enumerate(vote):
                teamVotes[team][pos] += 1
        
        return ''.join(sorted(teamVotes.keys(), reverse=True,
                              key=lambda team: (teamVotes[team], -ord(team))))