class Solution:
    def solution_1611_4(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        p, filled = sorted(passengers, reverse=True), set(passengers)
        last_p = 0
        
        for bus in sorted(buses):
            pop_cap = capacity
            while len(p) and p[-1] <= bus and pop_cap > 0:
                last_p = p.pop()
                pop_cap -= 1
                
        for spot in range(bus + 1 if pop_cap else last_p)[::-1]:
            if spot not in filled:
                return spot
                      
        return -1