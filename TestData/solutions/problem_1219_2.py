class Solution:
    def solution_1219_2(self, classes: List[List[int]], e: int) -> float:
        heap=[]
        for i,j in classes:
            diff=(i+1)/(j+1)-(i/j)
            heapq.heappush(heap,(-diff,i,j))
        while(e>0):
            diff,i,j=heapq.heappop(heap)
            i+=1
            j+=1
            diff=(i+1)/(j+1)-(i/j)
            heapq.heappush(heap,(-diff,i,j))
            e-=1
        ans=0
        for diff,i,j in heap:
            ans+=(i/j)
        return ans/len(classes)