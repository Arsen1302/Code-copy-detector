class Solution:
    def solution_216_2(self, num: int) -> str:
        Hex='0123456789abcdef' ; ans=''
        if num<0: num+=2**32
        while num>0: ans=Hex[num%16]+ans ; num//=16
        return ans if ans else '0'