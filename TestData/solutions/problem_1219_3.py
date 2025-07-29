class Solution:
    def solution_1219_3(self, classes: List[List[int]], extraStudents: int) -> float:
        H=[]
        for i in range(len(classes)):
            p,t=classes[i]
            heapq.heappush(H,(((p/t)-((p+1)/(t+1))),p,t))
        
        while extraStudents>0:
            x,y,z=heapq.heappop(H)
            y+=1
            z+=1
            heapq.heappush(H,(((y/z)-((y+1)/(z+1))),y,z))
            extraStudents-=1
        sm=0
        for x,y,z in H:
            sm+=(y/z)
        return sm/len(classes)