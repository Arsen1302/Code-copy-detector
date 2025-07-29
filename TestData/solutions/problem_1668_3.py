class Solution:
    def solution_1668_3(self, players: List[int], t: List[int]) -> int:
        
        c = j = i = 0
        players.sort()
        t.sort()
        while i <= len(players) - 1 and j <= len(t) - 1:
                if players[i] <= t[j]:
                    
                    c += 1
                    i += 1
                j += 1
         return c