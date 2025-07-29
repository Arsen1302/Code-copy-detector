class Solution:
    def solution_425_2(self, bits: List[int]) -> bool:
        i=0
        count=0
        while i<len(bits):
            if bits[i]==1:
                count=2
                i+=2
            else:
                count=1
                i+=1
        return count%2