class Solution:
    def solution_968_4(self, s: str) -> int:
        
        #Requirement : To find out the maximum length of a substring containining only unique character
        
        #Logic 1 : We will iterate over the string and if the current element == next element, we will increase our count. 
        #If its not, we will re-initialise the count to 1. To find out the maximum count among all the counts that came,
        #we will use an answer variable. 
        
        #Complexity Analysis - O(N) Time and O(1) Space
       
        n = len(s)
        
        if n == 1:
            return 1
        
        answer = 0 #this will hold our output 
        count = 1 #this will count the number of similar consecutive characters
        
        for i in range(0, n-1):
            if s[i] == s[i + 1]:
                count += 1 
            else:
                count = 1 
            answer = max(answer, count)
            
        return answer