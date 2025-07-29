class Solution:
    def solution_1219_4(self, classes: List[List[int]], extraStudents: int) -> float:
        pq = [(p/t - (p+1)/(t+1), p, t) for p, t in classes] # max-heap 
        heapify(pq)
        
        for _ in range(extraStudents):  
            _, p, t = heappop(pq)
            heappush(pq, ((p+1)/(t+1) - (p+2)/(t+2), p+1, t+1))
        
        return sum(p/t for _, p, t in pq)/len(pq)