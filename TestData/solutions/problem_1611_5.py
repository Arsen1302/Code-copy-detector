class Solution:
    def solution_1611_5(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses = sorted(buses)
        passengers = deque(sorted(passengers))
        res = buses[-1]
        
        s = set(passengers)
        prev = passengers[0]
        
        for i, bus in enumerate(buses):
            cap = capacity
            while cap and passengers and passengers[0] <= bus:
                val = passengers.popleft()
                prev = val
                cap -= 1
                if val-1 not in s:
                    res = val-1
                
            if cap:
                for k in range(bus, prev, -1):
                    if k not in s:
                        res = k
                        break
        
        return res