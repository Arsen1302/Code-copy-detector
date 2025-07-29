class Solution:
    def solution_1208_4(self, cars: List[List[int]]) -> List[float]:
        res = []
        ahead = [(math.inf, 0)]
        for pos, spd in reversed(cars):
            while ahead and spd <= ahead[-1][1]:
                ahead.pop()     
            atime = -1
            while len(ahead) >= 2:
                apos, aspd = ahead[-1]
                npos, nspd = ahead[-2]
                atime = (apos - pos)/(spd - aspd)
                ntime = (npos - pos)/(spd - nspd)
                if atime >= ntime:
                    ahead.pop()
                else:
                    break
            ahead.append((pos, spd))
            res.append(atime)
        res.reverse()
        return res