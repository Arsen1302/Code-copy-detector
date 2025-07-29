class Solution:
    def solution_1712_5(self, costs: List[int], k: int, can: int) -> int:
        l_heap,r_heap=[],[]
        ans=0
        n=len(costs)
        if n<=2*can:
            costs.sort()
            return sum(costs[:k])
        l_heap=costs[:can]
        r_heap=costs[n-can:]
        heapify(l_heap)
        heapify(r_heap)
        i,j=can,n-can-1
        while k:
            if not l_heap:
                ans+= heappop(r_heap)
                if i<=j:
                    heappush(r_heap,costs[j])
                    j-=1
            elif not r_heap or l_heap[0]<=r_heap[0]:
                ans+= heappop(l_heap)
                if i<=j:
                    heappush(l_heap,costs[i])
                    i+=1
            else:
                ans+= heappop(r_heap)
                if i<=j:
                    heappush(r_heap,costs[j])
                    j-=1
            k-=1
        return ans