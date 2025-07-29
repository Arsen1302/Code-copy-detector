class Solution:
    def solution_1567_5(self, tiles: List[List[int]], carpetLen: int) -> int:
        
        tiles.sort()

        starts, ends = [], []
        acc = [0]
        for a, b in tiles:
            starts.append(a)
            ends.append(b)
            acc.append(acc[-1] + b - a + 1)

        ans = 0
        for i, (a, b) in enumerate(tiles):
            # from start to right
            cover = min(tiles[-1][-1], a + carpetLen - 1)
            loc = bisect.bisect(starts, cover)
            if cover - starts[loc - 1] + 1 >= acc[loc] - acc[loc - 1]:
                ans = max(ans, acc[loc] - acc[i])
            else:
                ans = max(ans, acc[loc - 1] - acc[i] + cover - starts[loc - 1] + 1)
            
            # from end to left
            cover2 = max(tiles[0][0], b - carpetLen + 1)
            loc2 = bisect.bisect_left(ends, cover2)
            if ends[loc2] - cover2 + 1 >= acc[loc2+1] - acc[loc2]:
                ans = max(ans, acc[i + 1] - acc[loc2])
            else:
                ans = max(ans, acc[i + 1] - acc[loc2 + 1] + ends[loc2] - cover2 + 1)
            
        return ans