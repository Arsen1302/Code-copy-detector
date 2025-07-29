class Solution:
    def solution_1668_1_1(self, players: List[int], trainers: List[int]) -> int:
        n = len(players)
        m = len(trainers)
        players.sort()
        trainers.sort()
        dp = {}
        def solution_1668_1_2(i,j):
            if i==n or j==m:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            if players[i]<=trainers[j]:
                dp[(i,j)] = 1+solution_1668_1_2(i+1,j+1)
            else:
                dp[(i,j)] = solution_1668_1_2(i,j+1)
            return dp[(i,j)]
        return solution_1668_1_2(0,0)