class Solution:
    def solution_295_3(self, num: int) -> bool:
        return sum(set(reduce(lambda i,j:i+j ,([i,num//i] for i in range(1,int(num**0.5)+1) if num%i==0))))-num==num