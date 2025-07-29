class Solution:
def solution_896_3(self, events: List[List[int]]) -> int:
    
    m = 0
    for eve in events:
        m = max(m,eve[1])
    
    events.sort(key = lambda x:(x[0],x[1]))
    heap = []
    res = 0
    event_ind = 0
    
    n = len(events)
    for day in range(1,m+1):
        # Pushing all the events in heap that starts Today
        while event_ind<n and events[event_ind][0]==day:
            heapq.heappush(heap,events[event_ind][1])
            event_ind += 1
        
        # Poping all the events in heap that ends Today
        while heap and heap[0]<day:
            heapq.heappop(heap)
        
        # If any event is there which can be attended today then pop it and add it to res count.
        if heap:
            heapq.heappop(heap)
            res+=1
    
    return res