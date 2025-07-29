class Solution:
    def solution_745_4(self, trips: List[List[int]], capacity: int) -> bool:
        stops = []
        for num, from_, to in trips:
            stops.append((from_, num))
            stops.append((to, -num))
            
        stops.sort()            
            
        passengers = 0
        for _, num in stops:
            passengers += num
            if passengers > capacity:
                return False
            
        return True