class Solution:
    def solution_1708_3_1(self, n: int, target: int) -> int:
        #function to get sum of the number
        def solution_1708_3_2(n):
            return sum([int(i) for i in str(n)])
        
        #for the current digit place, if ones the 0, if tens then 1 as 10**1 =10
        level=0
        #storing ans
        toadd=0
        #calling function to get sum intially of n
        sm=solution_1708_3_2(n)

        #we need to loop till the sum is greater than target
        #take example of 467
        while(sm > target):
            #pick the last digit
            last = n%10
            #last == 464%10 => 7
            n+=(10-last)
            #467+=(10-7) == 470
            n=n//10
            #n==470//10 =>47
            toadd+=(10**level)*(10-last)
            #toadd= (10**0)*(10-7)=>3
            level+=1
            #level is now 1, for next iteration since we modified n only we need to keep
            #track of current digit place
            sm = solution_1708_3_2(n)
            #check the current sum again
        return toadd