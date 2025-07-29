class Solution:
    def solution_1565_5(self, num: int, k: int) -> int:
        c=0
        num_str=str(num)
        for i in range(len(num_str)-k+1):
            tmp=int(num_str[i:i+k])
            if tmp!=0:
                if num % tmp==0:
                    c+=1
        return c