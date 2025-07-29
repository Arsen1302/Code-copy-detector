class Solution:
    def solution_231_5(self, s: str, k: int) -> int:
        """
        
        s = ABAB
        k = 2
        
        If we have no limit on k then we can say that 
        (no of replacements to be done  = 
        length of string - count of character with maximum occurence)
        
        AAAAAABB -  Here 2 replacements to be done
        ABABABABAA - Here 4 replacements to be done
        
        Let's say there is a restriction on the number of updates done
        no. of replacements = len of str - min (count chars with max occur , k )
        
        If we change the problem statement from String to substring then we have to
        find the sustring of max length where atmost K repelacements can be done
        
        
        s = "AABABBA"
        k = 1
        
        i
        AABABBA count of max occur = 1 length of the substr = 1 repl = 0
        j
        
        i
        AABABBA count of max occur = 2 length of substr = 2 repl = 0
         j
         
        i
        AABABBA count max occur = 2 length of substr = 3 repl = 1
          j
        
        i
        AABABBA count max occur = 3 length of substr = 4 repl = 1
           j
           
        i
        AABABBA count max occur = 3 length of substr = 5 repl = 2
            j                       Here 2 > k => 2 > 1
                                    decrease window till repl becomes 1 again
         i
        AABABBA count max occur = 2 length of substr = 4 repl = 2
            j                          further decrease the window
            
          i   
        AABABBA count max occur = 2 length of substr = 3 repl = 1
            j
            
          i  
        AABABBA count max occur = 3 length of substr = 4 repl = 1
             j
             
          i
        AABABBA count max occur = 3 length of susbstr = 5 repl = 2 increase i
              j
            i  
        AABABBA    length of substr = 3
              j
              
              
    
        maximum length of substring with replacements that can be done = 1 is 4
        
        At any particular moment we need (max occur,length of substr,repl)
        
        """
        # In the below line we are keeping the count of each character in the string
        count = collections.Counter()
        # i : start of the window
        # j : end of the window
        i = j = 0
        # maxLen : maximum length of the substring
        maxLen = 0
        # maxOccur will store the count of max occurring character in the window
        maxOccur = None
        while j < len(s):
            # Increase the count of characters as we are increasing the window
            count[s[j]] += 1
            # maxOccur : count maximum occurring character in the window
            maxOccur = count[max(count , key = lambda x: count[x])]
            j += 1
            # length of substring - count of character with maximum occurence <= k
            while j - i - maxOccur > k :
                # We are decreasing the count here 
                count[s[i]] -= 1
                # Here we are again updating maxOccur
                maxOccur = count[max(count , key = lambda x: count[x])]
                # and then we are decreasing the window
                i += 1
            maxLen = max(maxLen , j - i)
        return maxLen
    
    # Time complexity is nearly O(n) as max operation can run for atmost 26 characters