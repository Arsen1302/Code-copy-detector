class Solution:
    def solution_1658_5(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n, max_robots = len(chargeTimes), 0
        max_charge = [] # max heap with tuples: (charge, index)
        running = runsum = 0
        p1 = p2 = cost = 0
        
        while p2 <= n:
            k = p2 - p1
            if cost <= budget:
                max_robots = max(max_robots, k)
            if p2 == n:
                break
                
			# pop any charge times that are not in the current window
            while max_charge and max_charge[0][1] < p1:
                heapq.heappop(max_charge)
                
            if cost <= budget: # add the next robot if we are within budget
                heapq.heappush(max_charge, (-chargeTimes[p2], p2))
                running += runsum + (k + 1) * runningCosts[p2]
                runsum += runningCosts[p2]
                cost = running - max_charge[0][0] # max heap stores negs
                p2 += 1
            
            elif k == 1:
                p1 = p2
                cost = running = runsum = 0
            
            else: # shrink window if budget is exceeded
                while max_charge and max_charge[0][1] <= p1:
                    heapq.heappop(max_charge)
                running -= runsum + (k - 1) * runningCosts[p1]
                runsum -= runningCosts[p1]
                cost = running - max_charge[0][0]
                p1 += 1
                
        return max_robots