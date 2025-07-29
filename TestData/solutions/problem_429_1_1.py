class Solution:
    def solution_429_1_1(self, graph, node, visit):
        visit.add(node)
        for nei in graph[node]:
            if nei not in visit:
                self.solution_429_1_1(graph, nei, visit)
        self.res.append(node)
    
    def solution_429_1_2(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = collections.defaultdict(set)
        for account in accounts:
            for email in account[1:]:
                graph[account[1]].add(email)
                graph[email].add(account[1])
        #print(graph.items())
        
        visit = set()
        ans = []
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in visit:
                    self.res = []
                    self.solution_429_1_1(graph, email, visit)
                    ans.append([name]+sorted(self.res))
        return ans