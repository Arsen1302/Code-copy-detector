class Solution:
    def solution_737_3(self, tiles: str) -> int:
        cur = set([''])
        for tile in tiles:
            nex = cur.copy()
            for word in cur:
                for j in range(len(word)+1):
                    nex.add(word[:j]+ tile +word[j:])
            cur = nex
        return len(cur)-1