class Solution:
    #T.C = O(n^2)
    #S.C = O(n)
    def solution_180_4(self, n: int) -> int:
        #The reason why this is a dp problem is because it exhibits
        #optimal substructure property!
        #Take for example n =2, we can take already existing single-digit 
        #unique numbers and simply add on unused digit in the least significant digit!
        # 1-> 12, 13, 14,..., 19
        # 2-> 21, 23, 24, 25, ..., 29
        #etc.
        #Basically, we can take each unique single digit number, whose single digits
        #are unique and consider using 9 other numbers in range 0-9 that has not
        #already been used -> thus, 10*9 + rem. subproblems from n-2 down to 1!
        
        #Furthermore, we may need to refer to already previously solved subproblems
        #for lower n when solving for current larger n-> Exhibits overlapping
        #subproblems property to apply dp!
        
        #edge case: n== 0, return 1 to avoid array index out of bounds error!
        if(n == 0):return 1
        
        #Take a bottom-up approach!
        #we need indices from 0 to n
        dp = [0] * (n+1)
        #add the dp-base
        dp[0] = 1
        dp[1] = 10
        
        #iterate through each subproblem or state's single parameter: current n value!
        digits_can_use = 9
        for i in range(2, n+1, 1):
            ans = 0
            prev_answer = dp[i-1]
            prev_answer *= digits_can_use
            ans += prev_answer
            #iterate from subproblem i-2 all the way down to subproblem 0 and add
            #the subproblem's answers to overall answer: other unaccounted numbers
            #in range from 0 to 10^n, not accounted for!
            for j in range(i-2, -1, -1):
                ans += dp[j]
            dp[i] = ans
            digits_can_use -= 1
        #then, our answer will be last element of dp table!
        return dp[n]