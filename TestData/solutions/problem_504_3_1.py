class Solution:
    #Time-Complexity: O(n^3), since outer for loop runs n times, and in worst case,
    #the first_value and second_value array of coordinates used to pairing up is in worst case
    #at most size n if the substring we passed to solution_504_3_2 is around n characters! 
    #Space-Complexity: O(2*n * n) -> O(n^2)
    def solution_504_3_1(self, s: str) -> List[str]:
        #First, we need to decide how to split s into two numbers! This will decide where to put
        #comma! 
        
        #Then, we need to see if we are able to put decimal point in only one of the two splitted
        #numbers!
        
        #we also need to exclude the parentheses characteres!
        s = s[1:len(s)-1]
        #we need to define some solution_504_3_2 to determine all possible valid coordinate values
        #we can form using substring x as input!
        def solution_504_3_2(x):
            #if x is single character, then itself is a valid coordinate value and only one!
            if(len(x) == 1):
                return [x]
            #if x has both first and last character be a 0, it can't ever result in a 
            #valid coordinate value!
            if(x[0] == "0" and x[len(x)-1] == "0"):
                return []
            #if only first character is 0, only valid coordinate value it can form is 
            #in form 0.xxxxxx...!
            if(x[0] == "0"):
                return ["0." + x[1:]]
            #if last digit is a 0, it can always be simplified no matter where I place
            #decimal point, thus only possible coordinate value candidate is x itself!
            if(x[-1] == '0'):
                return [x]
            #otherwise, we can simply generate all possible coordinate values by placing
            #decimal point between every two digits!
            else:
                #string x as itself is one of many ways!
                local = [x]
                #we will iterate from first char to 2nd to last char!
                cur = ""
                for i in range(0, len(x) - 1):
                    cur += x[i]
                    second_portion = x[i+1:]
                    overall = cur + "." + second_portion
                    local.append(overall)
                return local
                    
                    
                    
                    
            
        
        
        ans = []
        n = len(s)
        #For each iteration, we consider a possible split!
        for i in range(1, n):
            #consider splitting the string input s into left and right portions!
            #Left portion will determine all possible first coordinate values!
            #Right portion will determine all possible second coordinate values!
            l = s[:i]
            r = s[i:]
            #Once we find all possible first and second coordinate values, we simply
            #need to find all pairings!
            left_vals = solution_504_3_2(l)
            right_vals = solution_504_3_2(r)
            
            #before running for loop, we need to make sure that left_vals and right_vals is both
            #not an empty array. If even one of them is empty, it is not possible to form
            #a single valid 2-d coordinate pairing!
            if(not left_vals and not right_vals):
                continue
            for l in left_vals:
                for r in right_vals:
                    new_pairing = "(" + l + ", " + r + ")"
                    ans.append(new_pairing)
        return ans