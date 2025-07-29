class Solution:
    def solution_165_5(self, preorder: str) -> bool:
        
        preorder=preorder.split(",")
        stack=[]
        
        for node in preorder:
            stack.append(node)
            
            while len(stack)>2 and stack[-1]=="#" and stack[-2]=="#":
                if stack[-3]=='#':
                    return False
                stack=stack[:-3]
                stack.append(node)
        
        if len(stack)==1:
            if stack[-1]=="#":
                return True
        else:
            return False