class Solution:
    def solution_10_4_1(self, s: str, p: str) -> bool:
        
        dp = {}
        def solution_10_4_2(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            
            if i>=len(s) and j>=len(p):
                return True
            if i<= len(s) and j>= len(p):
                return False
            match  =  i< len(s) and ((s[i] == p[j]) or (p[j] == '.'))
            
            if j < len(p)-1 and  p[j+1] == '*':
                dp[(i,j)] = ( solution_10_4_2(i,j+2) # dont use *  
                    or (match and solution_10_4_2(i+1,j)) )
                return dp[(i,j)]
            if match:
                dp[(i,j)] = solution_10_4_2(i+1,j+1) 
                return dp[(i,j)]
        
        return solution_10_4_2(0,0)