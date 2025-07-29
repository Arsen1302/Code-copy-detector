class Solution:
    def solution_429_3_1(self, accounts: List[List[str]]) -> List[List[str]]:
        self.p = {i:i for i in range(len(accounts))} # parents
               
        eta = dict() # maps email to account
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in eta:
                    self.solution_429_3_2(eta[email], i)
                    continue
                
                eta[email] = i
    
        ate = dict() # maps account to emails
        for email in eta:
            acc = self.solution_429_3_3(eta[email])
            
            if acc in ate:
                ate[acc].append(email)
            else:
                ate[acc] = [email]
             
        res = []   
        for p in ate: # build the result list
            res.append([accounts[p][0]] + sorted(ate[p]))
            
        return res
    
    def solution_429_3_2(self, a, b):
        self.p[self.solution_429_3_3(b)] = self.solution_429_3_3(a)

    def solution_429_3_3(self, res):
        while self.p[res] != res:
            self.p[res] = self.p[self.p[res]]
            res = self.p[res]

        return res