class Solution:
    def solution_1340_4(self, piles: List[int], k: int) -> int:
        newPiles=[-1*i for i in piles]
        heapify(newPiles)
        while k>0:
            currEle=-1*heappop(newPiles)
            currEle-=(currEle//2)
            heappush(newPiles,-1*currEle)
            k-=1
        return -1*sum(newPiles)