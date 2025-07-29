class Solution:
    def solution_1439_1_1(self, bombs: List[List[int]]) -> int:
        if len(bombs)==1:
            return 1
        
        adlist={i:[] for i in range(len(bombs))}
        
        for i in range(len(bombs)):
            x1,y1,r1=bombs[i]
            for j in range(i+1,len(bombs)):
                x2,y2,r2=bombs[j]
                dist=((x2-x1)**2+(y2-y1)**2)**(1/2)
                if dist<=r1:
                    adlist[i].append(j)  
                if dist<=r2:
                    adlist[j].append(i)
        
        def solution_1439_1_2(adlist,seen,start):
            seen.add(start)
            for i in adlist[start]:
                if i not in seen:
                    solution_1439_1_2(adlist,seen,i)
        maxx=1   
        for v in adlist:
            seen=set()
            seen.add(v)
            solution_1439_1_2(adlist,seen,v)
            maxx=max(maxx,len(seen))
        return maxx