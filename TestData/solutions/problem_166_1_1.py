class Solution:
    def solution_166_1_1(self):
        self.path = []
    
    def solution_166_1_2(self, tickets: List[List[str]]) -> List[str]:
        flights = {}
        
        # as graph is directed
        # => no bi-directional paths
        for t1, t2 in tickets:
            if t1 not in flights:
                flights[t1] = []
                
            flights[t1].append(t2)

        visited = {}
        for k, v in flights.items():
            v.sort()
            visited[k] = [False for _ in range(len(v))]
        
        base_check = len(tickets) + 1
        routes = ['JFK']
        self.solution_166_1_3('JFK', routes, base_check, flights, visited)
        
        return self.path
        
        
    def solution_166_1_3(self, curr, routes, base_check, flights, visited):
        if len(routes) == base_check:
            self.path = routes
            return True
        
        # deadlock
        if curr not in flights:
            return False
        
        for idx in range(len(flights[curr])):
            if not visited[curr][idx]:
                visited[curr][idx] = True
                
                next_airport = flights[curr][idx]
                routes += [next_airport]
                result = self.solution_166_1_3(next_airport, routes, base_check,
                                    flights, visited)
                
                if result:
                    return True
                routes.pop()
                visited[curr][idx] = False

        return False