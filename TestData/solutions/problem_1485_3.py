class Solution:
    def solution_1485_3(self, startAt: int, moveCost: int, pushCost: int, t: int) -> int:
        res = []
        minu,min_sec = divmod(t,60)
        if minu <= 99:
            res.append([minu,min_sec])
        if min_sec + 60 <= 99 and minu -1 >= 0:
            res.append([minu-1,min_sec + 60])
            
        _min = inf
        res2 = []
        for m,s in res:
            if s < 10:
                s = str(0) + str(s)
            res2.append(int(str(m) + str(s)))
        for r in res2:
            c = 0
            r = str(r)
            if startAt != int(r[0]):
                c+=moveCost
            c+=pushCost
            for i in range(1,len(r)):
                if r[i] != r[i-1]:
                    c += moveCost
                c += pushCost
            
            _min = min(_min,c)
        return _min