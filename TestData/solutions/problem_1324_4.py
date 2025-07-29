class Solution:
    def solution_1324_4(self, times: List[List[int]], target: int) -> int:
        x,y=times[target]
        n=len(times)
        new=[]
        for i in range(0,n):
            heapq.heappush(new,i)
        heap=[]
        times.sort()
        min_heap=[]
        #print(times)
        
        for i,j in times:
            #print(heap,i,j)
            while(heap and heap[0][0]<=i):
                heapq.heappush(new,heapq.heappop(heap)[1])
                #heapq.heappop(heap)
            mini=heapq.heappop(new)
            if i==x and j==y:
                if heap==[]:
                    return 0
                else:
                    return mini
            heapq.heappush(heap,(j,mini))