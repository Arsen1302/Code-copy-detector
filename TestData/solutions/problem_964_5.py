class Solution:
    def solution_964_5(self, target: List[int], n: int) -> List[str]: 
        l=[] #will store stream of integers
        stack=[] #applying push and pop of elements
        ans=[] #answer -> storing operations
        x=0 #indexes for target
        j=0 #indexes for l
        for i in range(1,n+1): # list of stream of integers from 1 to n numbers
            l.append(i)

        while target!=stack and j<len(l): #stop operations when equal to target found or l come to an end
             
            stack.append(l[j]) #everytime a number get pushed until reached till the end of l
            ans.append("Push") #operation

            if len(stack)!=0 and stack[-1]!=target[x]: #if the stack element which is pushed recently is 
			#not same as target in that position theN pop the element 
                stack.pop()
                ans.append("Pop") #operation

            elif stack[-1]==target[x]: #if correct element pushed into stack then time to check for 
            #the next element of target for its equality with stack's position ,so increment the index of target
                x+=1 

            j+=1 #everytimr the next element will be chosen from the l till its end

        return ans