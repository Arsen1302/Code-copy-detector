class Solution:
    def solution_745_5(self, trips: List[List[int]], capacity: int) -> bool:        
        uber = []
        for psg, board, dest in trips:    #No. of passengers, start(boarding), end(destination)
            uber.append([board, psg])
            uber.append([dest, -psg])      
        heapq.heapify(uber)    
        while uber:
            loc, psg = heapq.heappop(uber)            
            capacity -= (psg)            
            if capacity < 0:
                return False        
        return True
        
		```