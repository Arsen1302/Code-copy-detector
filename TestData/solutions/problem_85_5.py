class Solution:
    def solution_85_5(self, n: int) -> int:
        b=bin(n).replace("0b","")[::-1]
        extra="".join([str(0)]*(32-len(b)))
        return int(b+extra,2)