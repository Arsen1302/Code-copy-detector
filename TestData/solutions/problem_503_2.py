class Solution:
    def solution_503_2(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target:
            return 0
        busstop=defaultdict(list)#List of Buses departing from every bus stops
        for busnum,stops in enumerate(routes):
            for stop in stops:
                busstop[stop].append(busnum)#'busnum' is departing from the bustop 'stop'
        q=[]
        visit=set()
        for bus in busstop[source]:#Grab all the buses departing from the source busstop
            q.append((bus,1))
            visit.add(bus)
        while q:
            busnum,numofbus=q.pop(0)
            if target in routes[busnum]:#If my target is in current bus route return the numofbus I have taken
                return numofbus
            for stops in routes[busnum]:#Get me all the stops for my current bus
                for buses in busstop[stops]:#Get me all the buses which departs from the stop of my current bus
                    if buses not in visit:#If I have not taken the bus add it to my queue
                        visit.add(buses)
                        q.append((buses,numofbus+1))
        return -1