class Solution:
def solution_995_2(self, arr: List[int], m: int) -> int:
    
    dic = Counter(arr)
    heap = []
    for k in dic:
        heapq.heappush(heap,(dic[k],k))
    
    while heap and m>0:
        f,k = heapq.heappop(heap)
        mi = min(m,f)
        m-=mi
        f-=mi
        
        if f!=0:
            heapq.heappush(heap,(f,k))
    
    return len(heap)