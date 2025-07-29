class Solution:
    def solution_701_3(self, s: str) -> str:
        c,j,n=0,0,len(s)
        ans=[]
        for i in range(n):
            if s[i]=='(':
                c+=1 #If there is opening paranthesis we increment the counter variable
            else:
                c-=1 #If there is closing paranthesis we decrement the counter variable
#If counter variable is 0 it means that No. of opening paranthesis = No. of closing paranthesis and we get a set of valid parethesis 
				if c==0:
#Once we get a valid set of parenthesis we store it in the list where j is the starting index of the valid parenthesis set and i is the last index.
#j+1 will remove the opening parenthesis and slicing the string till i(i.e., i-1) will store the valid set of parethesis in list after removing the outermost parenthis
                    ans.append(s[j+1:i])
                    j=i+1 #Changing the value of starting index for next valid set of parenthesis
        return ''.join(ans) #It will change the list into string