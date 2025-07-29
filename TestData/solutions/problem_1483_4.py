class Solution:
    def solution_1483_4(self, num: int) -> int:
        n=[num//1000,(num//100)%10,(num//10)%10,num%10] #This line will convert the four digit no. into array 
        n.sort() #It will sort the digits in ascending order
        return (n[0]*10+n[3])+(n[1]*10+n[2]) # Combination of first and last and the remaining two digits will give us the minimum value