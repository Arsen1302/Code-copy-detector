class Solution:

    def solution_503_4(self, routes: List[List[int]], source: int, target: int) -> int:
        # Step 0: Special case of an empty route
        if source == target: return 0

        # Step 1: Create a dict of [stop -> busses stopping at this stop]
        stop2bus = dict()
        for i in range(len(routes)):
            for stop in routes[i]:
                if stop not in stop2bus: stop2bus[stop] = set()
                stop2bus[stop].add(i)

        # Step 2: BFS over the bus stops
        bfs_queue = [(source,0)] # Tuple of (bus stop, number of busses taken to get to the stop)
        visited = {source} # Set of visited bus stops to avoid cycles
        
        while len(bfs_queue) > 0: # BFS
            stop, numBusses = bfs_queue.pop(0)
            if stop==target: return numBusses # If we arrived at the target, stop here!
            if stop in stop2bus:
                for bus in stop2bus[stop]: # Check all busses at this stop
                    for neighbour in routes[bus]: # Check all stops of each bus
                        if neighbour not in visited:
                            # Add all new stops to the neighbours
                            bfs_queue.append((neighbour,numBusses+1))
                            visited.add(neighbour)
                    routes[bus]=[]
            
        return -1 # If we finished the BFS and did not reach the target, it is unreachable