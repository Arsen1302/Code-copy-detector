class Solution:
    def solution_1662_5(self, n: int, meetings: List[List[int]]) -> int:
        d = dict()
        for i in range(n):
            d[i] = 0
        meetings = sorted(meetings,key = lambda x:(x[0],x[1]))
        room = [i for i in range(n)]
        for i in range(len(meetings)):
            flag=False
            for j in range(n):
                if room[j]<=meetings[i][0]:
                    room[j]=meetings[i][1]
                    d[j]+=1
                    flag=True
                    break
            if not flag:
                m=min(room)
                j=room.index(m)
                room[j]=room[j]+(meetings[i][1]-meetings[i][0])
                d[j]+=1
        c=0
        x=0
        for k,v in d.items():
            if v>c:
                x=k
                c=v
            elif v==c:
                x=min(x,k)
        return x