class Solution:
    def solution_1475_3(self, corridor: str) -> int:
        seat_idx = list()
        for i in range(len(corridor)):
            if corridor[i] == 'S':
                seat_idx.append(i)
                
        if len(seat_idx) == 0 or len(seat_idx) % 2:
		# if there are 0 or odd number of seats, we cannot divide sections with 2 seats each
            return 0
        
        ways = 1
        
        for i in range(2, len(seat_idx)-1, 2):  # ignore first and last seat
            ways *= seat_idx[i] - seat_idx[i-1]
        
        return ways % (10**9 + 7)