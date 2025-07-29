class Solution:
def solution_1372_4(self, n: int, rides: List[List[int]]) -> int:
    
    rides.sort()
    for ele in rides:
        ele[2] += ele[1]-ele[0]
        
    cp,mp = 0,0   # Current_profit, Max_profit
    heap=[]
    for s,e,p in rides:
        while heap and heap[0][0]<=s:
            et,tmp = heapq.heappop(heap)
            cp = max(cp,tmp)
        heapq.heappush(heap,(e,cp+p))
        mp = max(mp,cp+p)
    return mp