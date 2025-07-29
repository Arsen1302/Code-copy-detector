class Solution:
    def solution_553_4_1(self, N: int) -> int:
        '''
        1. If N<=11, then the result is the first prime number greater than or equal N
        2. If 11<N<=101, then the result is 101
        3. Otherwise, there are no prime palindromes of even length
        4. Let N is a x' digit number. If x' is even, then set N=10^x'. Now N is x=x'+1 digit number where x is odd. If x' is odd, then don't change N and here x=x'.
        5. Starting from N, generate palindromes and check if it is prime
        6. If not, then set N = value of first floor(x//2) digits + 1, and go back to step 4 and generate new palindromes from new N.
        '''
        
        def solution_553_4_2(n):                             
            i=3                                                                                     #don't need to check any even number, so start checking from 3
            while i*i<=n:                                                                           #if n is not prime, then it will be divisible by a number at most sqrt(n)
                if n%i==0:
                    return False                                                                    #has divisor, so not prime
                i+=2                                                                                #only check if there are odd divisors, as n is odd
                
            return True                                                                             #n is prime
        
        if N==1 or N==2:                                                                            #nearest prime number of N in {1,2} is 2 which is palindrome
            return 2
        
        elif N==3:                                                                                  #3 is a prime palindrome
            return 3
        
        elif N==4 or N==5:                                                                          #nearest prime number of N in {4,5} is 5 which is palindrome
            return 5
        
        elif N==6 or N==7:                                                                          #nearest prime number of N in {6,7} is 7 which is palindrome
            return 7
        
        elif N>7 and N<=11:                                                                         #nearest prime number of N greater than 7 is 11 which is palindrome
            return 11
        
        elif N>11 and N<=101:                                                                       #for all two digit numbers greater than 11, and for 100,101
            return 101                                                                              #nearest prime palindrome is 101
        
        start=(N+1)*(N%2==0)+N*(N%2==1)                                                             #prime number must be odd, so start checking from the odd number nearest to N
        len_string =len(str(start))
        str_N = str(start)
        
        if str_N==str_N[::-1] and solution_553_4_2(start):                                                   #if N or (N+1) is prime, then don't need to check further
            return start
                
        else:    
            while(True):
                if len_string%2==0:
                    start=10**(len_string)                                                          #convert even length starting number to odd length
                    str_N=str(start)                                                                #store the string representation of starting number
                
                if int(str_N[0])%2==0:                                                              #if the first digit is even, then the palindrome will also be even
                    start+=10**(len_string-1)                                                       #start from the nearest number whose first digit is odd                                          
                    str_N=str(start)
                    
                if int(str_N[0])==5:                                                                #if the first digit is 5, then the palindrome is divisible by 5
                    start=7*(10**(len_string-1))                                                    #the nearest prime palindrome starts with 7                                          
                    str_N=str(start)
                                                                                                    
                str_N = str_N[0:len_string//2]+str_N[len_string//2]+str_N[0:len_string//2][::-1]    #create palindrome closest to starting number
                    
                if int(str_N)>=N and solution_553_4_2(int(str_N)):
                    return int(str_N)                                                               #got a palindrome greater than or equal N, return the palindrome
                else:
                    start=int(str_N[0:len_string//2+1])+1                                           #increase the value of starting floor(len_string//2) digits by one   
                    start*=10**(len_string//2)                                                      #append necessary 0's to start and this will be the new starting position
                    
                    str_N=str(start)                                                                #convert start to string
                    len_string=len(str_N)                                                           #store the length