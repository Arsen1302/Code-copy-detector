class Solution:
    def solution_1611_2(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        prev = -inf 
        queue = deque()
        prefix = i = j = 0 
        while i < len(buses) or j < len(passengers): 
            if i == len(buses) or j < len(passengers) and passengers[j] <= buses[i]: 
                if j == 0 or passengers[j-1] + 1 < passengers[j]: prev = passengers[j]-1
                prefix += 1
                if prefix and prefix % capacity == 0: queue.append(prev)
                j += 1
            else: 
                if prefix < capacity: 
                    if j == 0 or buses[i] != passengers[j-1]: ans = buses[i]
                    else: ans = prev 
                    prefix = 0 
                elif queue: 
                    ans = queue.popleft()
                    prefix -= capacity 
                i += 1
        return ans