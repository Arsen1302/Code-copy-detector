class Solution:
    def solution_1340_5(self, piles: List[int], k: int) -> int:
        
        # since python provides only min heap, we need to make all the elements negative
        # so that it can be utilized as a max heap
        
        for i in range(len(piles)):
            piles[i]=-piles[i]
        q=heapq.heapify(piles) 
        
        while k>0:
            
            p=heapq.heappop(piles)
            # since the elements are negative, we need to use ceil instead of floor
            p=p-(math.ceil(p/2))
            
            heapq.heappush(piles,p)
            
            k-=1
            
        return -sum(piles)