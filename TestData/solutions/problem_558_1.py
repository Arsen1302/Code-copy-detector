class Solution:          # Here's the plan:
                         # 
                         # 1) We only need to be concerned with two quantities: the dist traveled (pos)
                         #    and the fuel acquired (fuel). We have to refuel before pos > fuel.
                         # 
                         # 2) Because  we have an infinite capacity tank, we only have to plan where to acquire
                         #    fuel before pos > fuel, and common sense says to stop at the station within range
                         #    with the most fuel.
                         # 
                         # 3) And that's a job for a heap. we heappush the stations that are within range of present
                         #    fuel, and heappop the best choice if and when we need fuel.
                         #  
                         # 4) We are finished when a) we have acquired sufficient fuel such that fuel >= target 
                         #    (return # of fuelings), or b) fuel < target and the heap is empty (return -1).
                       
    def solution_558_1(self, target: int, startFuel: int, stations: List[List[int]]) -> int:

        fuel, heap, count = startFuel, [], 0            # <-- initialize some stuff
        
        stations.append([target, 0])                    # <-- this handles the "stations = []" test

        while stations:
            if fuel >= target: return count             # <-- 4)            

            while stations and stations[0][0] <= fuel:  # <-- 3)
                _, liters = stations.pop(0)
                heappush(heap,-liters)

            if not heap: return -1                      # <-- 4)
            fuel-= heappop(heap)

            count+= 1