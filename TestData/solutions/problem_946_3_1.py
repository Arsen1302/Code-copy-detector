class Solution:
    def solution_946_3_1(self, n: int, k: int) -> str:
        res=[]
        inp_string=['a','b','c']
   
        def solution_946_3_2(index,string):
            if len(string)==n:
                res.append(string)
                return
            for i in range(len(inp_string)):
                if len(string)==0:
                    solution_946_3_2(i,string+inp_string[i])
                else:
                    if string[-1]==inp_string[i]:
                        continue
                    solution_946_3_2(i,string+inp_string[i])
           
        solution_946_3_2(0,'')
        if k<=len(res):
            return res[k-1]
        else:
            return ''