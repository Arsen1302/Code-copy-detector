class Solution:
    def solution_1534_5(self, matches: List[List[int]]) -> List[List[int]]:
        # Consider two HashMaps g  is #games and w is #wins 
        # if g[k] - w[k] =0. Then all games are won 
        # if g[k] - w[k] =1. Then all games are won except 1 game (ie. exactly 1 fail)
        from collections import defaultdict
        g,w = defaultdict(int), defaultdict(int)
        
        allTeams =set()
        for aGame in matches:
            winner,looser = aGame[0], aGame[1]
            g[winner] +=1 
            g[looser] +=1
            w[winner] +=1
            allTeams.add(winner)
            allTeams.add(looser)
            
        allTeams = sorted(allTeams)
        
        allwin,onefail = [],[]
        for aTeam in allTeams:
            if g[aTeam] - w[aTeam] ==0:
                allwin.append(aTeam)
            if g[aTeam] - w[aTeam] ==1:
                onefail.append(aTeam)
        
        return [allwin,onefail]