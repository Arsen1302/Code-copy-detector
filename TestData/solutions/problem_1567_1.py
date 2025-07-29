class Solution:
    def solution_1567_1(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        ans = ii = val = 0 
        for i in range(len(tiles)): 
            hi = tiles[i][0] + carpetLen - 1
            while ii < len(tiles) and tiles[ii][1] <= hi:
                val += tiles[ii][1] - tiles[ii][0] + 1
                ii += 1
            partial = 0 
            if ii < len(tiles): partial = max(0, hi - tiles[ii][0] + 1)
            ans = max(ans, val + partial)
            val -= tiles[i][1] - tiles[i][0] + 1
        return ans