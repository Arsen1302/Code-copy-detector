class Solution:
    def solution_126_4_1(self, input: str) -> List[int]:
        
        
        def solution_126_4_2(string):
            
            result=[]
            
            for i, c in enumerate(string):
                
                if c in "+-*":
                    x=solution_126_4_2(string[:i])
                    y=solution_126_4_2(string[i+1:])
                    
                    for a in x:
                        for b in y:
                            
                            if c=='+':
                                result.append(a+b)
                            elif c=='-':
                                result.append(a-b)
                            else:
                                result.append(a*b)
                                
            if not result:
                return [int(string)]
            
            return result
        
        return solution_126_4_2(input)