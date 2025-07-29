class Solution:
    def solution_729_4(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        #sliding window technique!
        #first, linearly traverse customers array and see number of customers that are 
        #gauranteed to be satisfied regardless of store owner's powerup!
        
        #then, use sliding window and maximize the number of customers that can be converted 
        #to satisfied by using minutes amount of power up !
        
        #If we let len(customers)=n and len(grumpy) = m,
        #Time: O(2n) -> O(n)
        #Space: O(1)
        
        
        #add these 2 results and that is the answer!
        #Step 1
        ans = 0
        for a in range(len(customers)):
            if(grumpy[a] == 0):
                ans += customers[a]
        #step 2: sliding window!
        
        L, R = 0, 0
        converted = 0
        maximum = 0
        length = 0
        while R < len(customers):
            #process right element
            if(grumpy[R] == 1):
                converted += customers[R]
            length += 1
            #stopping condition: if length ever reaches minutes
            while length == minutes:
                #process current sliding window!
                maximum = max(maximum, converted)
                #shrink the sliding window!
                #check if left minute is the minutes store owner is grumpy!
                if(grumpy[L] == 1):
                    converted -= customers[L]
                length -= 1
                L += 1
            #keep expanding sliding window
            R += 1
        return maximum + ans