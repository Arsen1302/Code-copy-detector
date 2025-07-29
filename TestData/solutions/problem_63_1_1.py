class Solution:
    def solution_63_1_1(self, tokens: List[str]) -> int:
        
        def solution_63_1_2(sign):
            n2,n1=stack.pop(),stack.pop()
            if sign=="+": return n1+n2
            if sign=="-": return n1-n2
            if sign=="*": return n1*n2
            if sign=="/": return int(n1/n2)
			
        stack=[]
        
        for n in tokens:
            if n.isdigit() or len(n)>1:
                stack.append(int(n))
            else:
                stack.append(solution_63_1_2(n))
        return stack.pop()