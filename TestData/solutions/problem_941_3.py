class Solution:
    def solution_941_3(self, queries: List[int], m: int) -> List[int]:
        res=[]
        p=[]
        
        for i in range(1,m+1):
            p.append(i)
            
        
        for i in range(len(queries)):
            
            num = queries[i] # 3
            idx = p.index(num) # get Index of 3 from P
            res.append(idx)
            
            temp=p[idx]  #store 3 in temp
            del p[idx]  # delete 3 from P
            
            p.insert(0,temp) # Insert 3 in P at position 0 i.e. -> Starting
            
        return res