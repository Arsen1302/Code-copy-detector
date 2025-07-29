class Solution:
    def solution_1662_2_1(self, n: int, meetings: List[List[int]]) -> int:
        currentMeetHeap = []
        numOfMeet = n * [0]
        currentMeet = n * [False]
        meetings.sort()
        
        # Removes ended meetings from the heap.
        def solution_1662_2_2(cutoff): 
            while len(currentMeetHeap)>0 and cutoff>=currentMeetHeap[0][0]:
                ended = heapq.heappop(currentMeetHeap)
                currentMeet[ended[1]] = False
            
        def solution_1662_2_3(room, end):
            currentMeet[room] = True
            numOfMeet[room] += 1
            heapq.heappush(currentMeetHeap, [end,room])
        
        def solution_1662_2_4():
            maxMeet = 0
            maxMeetRoom = 0
            for i in range(len(numOfMeet)): 
                meets = numOfMeet[i]
                if meets > maxMeet: 
                    maxMeet = meets
                    maxMeetRoom = i
            return maxMeetRoom
            
            
        for meeting in meetings:
            # First check if theres any empty rooms at the start of the current meeting.
            # If so, use this room.
            solution_1662_2_2(meeting[0])
            added = False
            for i in range(n):
                if not currentMeet[i]:
                    solution_1662_2_3(i, meeting[1])
                    added = True
                    break
            if (added):
                continue
				
            # If no meeting rooms initially available, pull a meeting from the heap. 
            # We need to adjust the end time to account for the wait. 
            firstAvailable = heapq.heappop(currentMeetHeap)
            solution_1662_2_3(firstAvailable[1], meeting[1]+(firstAvailable[0]-meeting[0]))
        
        return solution_1662_2_4()