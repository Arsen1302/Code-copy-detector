class Solution:
    def solution_1658_4(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        i = 0 
        j = 0
        maxi = 0
        total = 0
        maxHeap = []
        heapq.heapify(maxHeap)
        prev = 0
        maxj = 0
        prefix = [0]*len(chargeTimes)
        while i<=j and j < len(chargeTimes):
            if total>=budget:
                maxHeap.remove(-1*chargeTimes[i])
                i+=1
            heapq.heappush(maxHeap,-1*chargeTimes[j])
            prefix[j] = prev + runningCosts[j]
            prev = prefix[j]
            max_charge = -1*maxHeap[0]
            if i == 0 :
                running = prefix[j]
            elif i==j:
                running = runningCosts[j]
            else:
                running  = prefix[j] -prefix[i-1]
            total = max_charge + (j-i+1) * running
            if total<=budget:
                maxi = max(maxi,j-i+1)
            j+=1            
        return maxi