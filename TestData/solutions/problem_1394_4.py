class Solution:
    def solution_1394_4(self, edges: List[List[int]], patience: List[int]) -> int:
        #part-1 of code
        #Djikstra for getting the shortest time
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        time_tracker = [float("inf")]*len(patience)
        time_tracker[0] = 0

        heap = []
        heappush(heap,(0,0))

        while heap:
            time,node = heappop(heap)
            for nei in graph[node]:
                if time+1 < time_tracker[nei]:
                    heappush(heap,(time+1,nei))
                    time_tracker[nei] = time+1
        
        #part-2 of code
        #To find the max time needed
        max_time_needed = 0
        for i in range(1,len(time_tracker)):
            #time needed will be 2 times what it takes one way
            time_needed = 2*time_tracker[i]
            #number of msgs sent will me time_needed/patience
            #why ceil? if time_needed -> 6 and patience -> 5
            #time_needed/patience -> 1.2, we can send 0.2 msg,we have
            #to send entire msg. So we take ceil
            msgs_sent = ceil(time_needed/patience[i])
            #total time needed will be the time when last msg is sent
            #plus the time it will take to come back(i.e. time_needed)
            #the first msg is sent at 0th second. that leaves us with
            #msgs_sent - 1. We multiply it by patience to get when
            #the last msg will be sent. 
            total_time_needed = (patience[i])*(msgs_sent-1) +time_needed
            max_time_needed = max(max_time_needed,total_time_needed)

        return max_time_needed + 1