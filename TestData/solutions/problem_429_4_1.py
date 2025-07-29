class Solution:
    def solution_429_4_1(self):
        self.accountConnections = defaultdict(set)
        self.emailToName = dict()
        self.seen = set()
    
    def solution_429_4_2(self, accounts):
        for account in accounts:
            name = account[0]
            key = account[1]
            for i in range(1, len(account)):
                self.accountConnections[key].add(account[i])
                self.accountConnections[account[i]].add(key)
                self.emailToName[account[i]] = name
                
    def solution_429_4_3(self, accountNode):
        if accountNode in self.seen:
            return []
        
        self.seen.add(accountNode)
        connections = self.accountConnections[accountNode]
        result = [accountNode]
        
        for connection in connections:
            result += self.solution_429_4_3(connection)
        
        return result
    
    def solution_429_4_4(self, accounts: List[List[str]]) -> List[List[str]]:
        self.solution_429_4_2(accounts)
        mergedAccounts = []
        
        for account in self.accountConnections:
            localMerge = self.solution_429_4_3(account)
            name = self.emailToName[account]
            if localMerge:
                localMerge.sort()
                mergedAccounts.append([name] + localMerge)
        
        return mergedAccounts