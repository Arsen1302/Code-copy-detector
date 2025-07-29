class Solution:
    def solution_1485_5(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        mins1,secs1 = (0,targetSeconds) if targetSeconds<100 else (targetSeconds//60,targetSeconds%60)
        if mins1>99:
            mins1 -= 1
            secs1 += 60
        l = [(mins1,secs1)]
        if mins1>0 and secs1<40:
            mins2 = mins1-1
            secs2 = secs1+60
            l.append((mins2,secs2))
        if mins1<99 and secs1>=60:
            mins2 = mins1+1
            secs2 = secs1-60
            l.append((mins2,secs2))
        ret = inf
        for mins,secs in l:
            mins = str(mins) if mins>0 else ''
            if secs>=10:
                secs = str(secs)
            else:
                if mins:
                    secs = '0'+str(secs)
                else:
                    secs = str(secs)
            t = mins+secs
            #print(t)
            total = 0
            for i in range(len(t)):
                if i==0 and t[i]==str(startAt):
                    total += pushCost
                elif i>0 and t[i]==t[i-1]:
                    total += pushCost
                else:
                    total += moveCost + pushCost
            ret = min(ret,total)
        return ret