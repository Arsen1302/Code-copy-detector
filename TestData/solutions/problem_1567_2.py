class Solution:
    def solution_1567_2(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles = sorted(tiles, key = lambda x : x[0])
        prefix_sum = [0]
        res = 0
        for idx, (start, end) in enumerate(tiles):
            cur_cover = 0
            prefix_sum.append(prefix_sum[-1] + (end - start + 1))
            begin = max(0, end - carpetLen + 1)
            l, r = -1, len(tiles)
            while l + 1 < r:
                mid = (l + r) // 2 # >> 1
                if tiles[mid][0] <= begin:
                    l = mid
                else:
                    r = mid
            if tiles[max(0, l)][0] <= begin <= tiles[max(0, l)][1]:
                cur_cover += tiles[l][1] - begin + 1
            cur_cover += prefix_sum[idx + 1] - prefix_sum[l + 1]
            res = max(res, cur_cover)
        return res