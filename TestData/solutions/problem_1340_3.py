class Solution:
    def solution_1340_3(self, piles: List[int], k: int) -> int:
        for i, val in enumerate(piles): #we need maxheap, so negate all values
            piles[i]=-val
        heapify(piles)
        while k:
            x = -heappop(piles) #pop largest absolute no. 
            x-=(x//2) 
            heappush(piles,-x) #negate value before pushing
            k-=1
        return sum(piles)*-1 #all values are negative so use abs or multiply with -1