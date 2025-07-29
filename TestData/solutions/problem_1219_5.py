class Solution:
    def solution_1219_5(self, classes: List[List[int]], extraStudents: int) -> float:
        pq = []
                  
        for i, stat in enumerate(classes):
            score = (stat[1]-stat[0])/(stat[1]*(stat[1]+1))
            heapq.heappush(pq, (-score, i))
            
        while extraStudents:
            _, idx = heapq.heappop(pq)
            
            classes[idx][0] += 1
            classes[idx][1] += 1
            newScore = (classes[idx][1]-classes[idx][0])/(classes[idx][1]*(classes[idx][1]+1))
            heapq.heappush(pq, (-newScore, idx))
            
            extraStudents -= 1
            
        return sum(stat[0]/stat[1] for stat in classes)/len(classes)