class Solution:
    def solution_590_3_1(self, x: int) -> bool: # return whether x am solution_590_3_1
        rev = 0
        normal = x
        while x:
            rev = rev*10 + x%10 # push last digit to 'rev'
            x = x//10           # remove last digit
        return rev == normal
	 # O(root(n) x log (n)) -> since i generate left half until square(left_half+right_half) reaches
     # the 'right' now, why is this passing and below solution TLE? because here i only generate palindromes!
    def solution_590_3_2(self, left: str, right: str) -> int:
        left, right = int(left), int(right)
        
        # guess the half of every palindrome, 
        # generate the other half (reverse)!
        
        left_half = 1 
        ans = 0
        
        while True: # no need of MAGIC, just stop when all my options > right
            
            right_half = str(left_half)[::-1] 
            
            even_palindrome = int(str(left_half) + right_half)
            
            odd_palindrome = int(str(left_half) + right_half[1:])
            
            # print(even_palindrome, odd_palindrome)
            
            even_pal_sqr = even_palindrome*even_palindrome
            odd_pal_sqr  = odd_palindrome*odd_palindrome
            
            # if (in range) AND (is a palindrome)
            if left <= even_pal_sqr <= right and self.solution_590_3_1(even_pal_sqr):
                ans += 1
            
            if left <= odd_pal_sqr <= right and self.solution_590_3_1(odd_pal_sqr):
                ans += 1
                
            # no more palindromes will be found!
            if even_pal_sqr > right and odd_pal_sqr > right:
                return ans
            
            left_half += 1
            
    def solution_590_3_3(self, left: str, right: str) -> int:
        
        left, right = int(left), int(right)
        check = floor(sqrt(left))
        
        while check*check < left:
            check += 1
        
        res = 0
        while check*check <= right:
            if self.solution_590_3_1(check) and self.solution_590_3_1(check*check):
                res += 1
            check += 1
        return res