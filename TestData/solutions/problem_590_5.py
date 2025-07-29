class Solution:
    def solution_590_5(self, left: str, right: str) -> int:
        left,right = int(left),int(right)
		#Just to travese the loop declare a variable and set the limit
        limit = 100000
		#to count super Palindromes
        cnt = 0
		#count odd number length palindromes
        for i in range(1,limit):
			# to add the the numbers it easily I have converted it to string
            s = str(i)
			# add s with s in the reverse order by leaving the 1st element so that we will get odd number length string
            p = s+s[::-1][1:]#or U can use negative indexing s[-2::-1]
			#square the number we got
            p2 = int(p) ** 2
			#if the squares number of p is greater than right value break the loop
            if p2 > right:
                break
			#if squared value of p is greater than or equal to left and and the reversal of that squares value is also a palindrome then increase the count
            if p2 >=left and str(p2) == str(p2)[::-1]:
                #print(p,p2)
                cnt += 1
		#to count even number length palindromes
        for i in range(limit):
			# to add the the numbers it easily I have converted it to string
            s = str(i)
			# add s with s in the reverse order so that we will get even number length string
            p = s + s[::-1]
			#square the number we got
            p2 = int(p) ** 2
			#if the squares number of p is greater than right value break the loop
            if p2 > right:
                break
			#if squared value of p is greater than or equal to left and and the reversal of that squares value is also a palindrome then increase the count
            if p2 >= left and str(p2) == str(p2)[::-1]:
                #print(p,p2)
                cnt += 1
        return cnt