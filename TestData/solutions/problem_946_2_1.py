class Solution:
    def solution_946_2_1(self,s , l , letters , n ):
        if(len(s) == n):
            l.append(s)
            return 0
        for i in letters :
            if(s[-1] != i ):
                self.solution_946_2_1(s + i , l , letters , n)
            
        
            
    def solution_946_2_2(self, n: int, k: int) -> str:
        letters = ["a" , "b" , "c"]
        l = []
        for i in letters :
            self.solution_946_2_1(i,l,letters , n)
            if(len(l) >= k):
                return l[k-1]
        return ""