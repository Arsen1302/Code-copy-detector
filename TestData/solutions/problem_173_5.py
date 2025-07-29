class Solution:
    #Time-Complexity: O(n^2)
    #Space-Complexity: O(n)
    def solution_173_5(self, n: int) -> int:
        #we know we can reduce n as 
        # n
    #   /  \
    #  1   n-1
    #     /  \
    #    1   n-2
    #     ...
    
        #Basically, we can keep reducing n like this in this tree structure above!
        #This is the pattern I recognized! I recognized for given n, there are 
        #potential sums of (1, n-1), (2, n-2), (3, n-3), ..., (n//2, n//2)!
        #For each pair, I can compare the direct number with the max product decomposition
        #and take the max of two!
        
        
        #Reason for comparison: for each of the sum factor of given n, either leave it
        #undecomposed or decompose it into further sum factors if the product of sum
        #factors produce ultimately a number that exceeds the orignal sum factor! This way
        #I am maximing product contribution for each and every sum factor!
        
        #For example, for 5, we decompose it into 2 and 3, since 2*3 > 5, so it will
        #maximize our product further!
        
        #However, for 3, we don't decompose since we can maximally decompose to
        #1 and 2 but 1*2 < 3!
        
        #Do that for both numbers of each pair and take the product!
        #Whatever is largest across the pairs will be answer for given input n!
    
        dp = [-1] * (n+1)
        #add dp-base!
        dp[1] = 1
    
        #this problem has only one state parameter: the given number to start decomposing           #from!
        #iterate through each subproblem or state!
        #Bottom-Up
        for i in range(2, n+1, 1):
            upper_bound = (i // 2) + 1
            #iterate through all possible pairs!
            for j in range(1, upper_bound, 1):
                #current pair (j, i-j), which we probably already solved its subproblems!
                first = max(j, dp[j])
                second = max(i-j, dp[i-j])
                #get product for current pair!
                sub_ans = first * second
                #compare current pair's product against built up answer maximum!
                dp[i] = max(dp[i], sub_ans)
    
        #then, once we are done, we can return dp[n]!
        return dp[n]