class Solution:
    def solution_1662_4(self, n: int, meetings: List[List[int]]) -> int:
        
        cnt = [0] * n
        
        available = list(range(n))
        heapify(available)
        
        used = []        
        meetings.sort(reverse=True)
        
        while meetings:
            start, end = meetings.pop()
            # backfill room into available 
            while used and used[0][0] <= start:
                _, room = heappop(used)
                heappush(available, room)            
            
            if available:
                room = heappop(available)
                heappush(used, (end, room))
                cnt[room] += 1
				
            # if no available room, means all current used room will end after curret meeting start time
            # then pop out the earliest and smallest room number, new end time will be the popped end time + meeting duration
            else:
                room_end, room = heappop(used)
                heappush(used, (room_end+end-start, room))
                cnt[room] += 1

        
        return cnt.index(max(cnt))