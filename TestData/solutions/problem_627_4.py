class Solution:
    def solution_627_4(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        index=0
        n=len(pushed)
        for i in pushed:
            stack.append(i)
            
            while len(stack)>0 and index<n and popped[index]==stack[-1]:
                stack.pop()
                index+=1
        return index==n