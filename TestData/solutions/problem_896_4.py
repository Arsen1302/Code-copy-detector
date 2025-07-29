class Solution:
    def solution_896_4(self, events: List[List[int]]) -> int:
        # 1. person can only attend one event per day, even if there are multiple events on that day.
        # 2. if there are multiple events happen at one day,
        #    person attend the event ends close to current day.
        #.   so we need a data structure hold all the event happend today,
        #    and sorted ascedningly. minimum heap is the data structure we need.
        
        """
       [[1,1],[1,2],[2,2],[3,4],[4,4]]
       day one events: [1,1] [1,2]
                       events today:             heap = [1,2]
                       events expire today: none,heap = [1,2]
                       events attend: 1,         heap = [2]
       day two events: [1,2],[2,2]
                       events today:             heap = [2,2]
                       events expire today:none, heap = [2,2]
                       events attend: 2          heap = [2]
       day three events: [2,2][3,4]
                       events today:             heap = [2,4]
                       events expire today;[1,2] heap = [4]
                       events attend:3           heap = []
        """
        events = sorted(events,key = lambda x:(x[0],x[1]))  
        #determine the number of days has events
        n = 0
        for i in range(len(events)):
            n = max(n,events[i][1])
            
        attended = 0
        day =  0
        eventIdx = 0
        heap =[]
        
        
        for day in range(1, n + 1):
            #step 1: Add all the events ending time to the heap that start today
            while eventIdx < len(events) and events[eventIdx][0] == day:
                heappush(heap,events[eventIdx][1])
                eventIdx += 1
            
            #step 2: Remove the events expired today
            while heap and heap[0] < day:
                heappop(heap)
            
            #step 3: event that can be attended today,only one event per day.    
            if heap:
                heappop(heap)
                attended += 1
            
        return attended