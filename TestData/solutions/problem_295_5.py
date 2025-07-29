class Solution:
    def solution_295_5(self, num: int) -> bool:
        return False if num==1 else num-1==sum([i+num//i for i in range(2,int(sqrt(num))+1) if num%i==0])