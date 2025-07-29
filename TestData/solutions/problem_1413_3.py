class Solution:
def solution_1413_3(self, n, A):
    
    heap = []
    for q in A:
        heapq.heappush(heap,(-q,1))
        n-=1
        
    while n>0:
        quantity,num_shops = heapq.heappop(heap)
        total = (-1)*quantity*num_shops
        num_shops+=1
        n-=1
        heapq.heappush(heap,(-1*(total/num_shops),num_shops))
    
    return math.ceil(-heap[0][0])

**Thanks and Upvote if You like the Idea !! 🤞**