class Solution:
    def solution_897_2(self, target: List[int]) -> bool:
        if len(target) == 1: return target[0] == 1 # edge case 
        
        total = sum(target)
        pq = [-x for x in target] # max heap 
        heapify(pq)
        
        while -pq[0] > 1: 
            x = -heappop(pq)
            total -= x
            if x <= total: return False 
            x = (x-1) % total + 1
            heappush(pq, -x)
            total += x
        return True