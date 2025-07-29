class Solution:
    def solution_1500_3(self, s: str, repeatLimit: int) -> str:
        count = collections.Counter(s)
        chrs = list(map(list, sorted(count.items(), reverse=True)))
        res = []
        first, second = 0, 1
        n = len(chrs)
        
        while second < n:
            if chrs[first][1] <= repeatLimit:
                res.append(chrs[first][0] * chrs[first][1])
                first += 1
                while chrs[first][1] == 0:
                    first += 1
                if first >= second:
                    second = first + 1
            else:
                res.append(chrs[first][0] * repeatLimit + chrs[second][0])
                chrs[first][1] -= repeatLimit
                chrs[second][1] -= 1
                if chrs[second][1] == 0:
                    second += 1
        
        res.append(chrs[first][0] * min(repeatLimit, chrs[first][1]))
        return ''.join(res)