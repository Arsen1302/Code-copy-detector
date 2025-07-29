class Solution:
    def solution_1269_3_1(self,lis):
        if lis == []:
            return 0
        if len(lis) == 1:
            return lis[0]
        xor = 0
        for i in lis:
            xor ^= i
        return xor
    def solution_1269_3_2(self,seq):
        if len(seq) <= 0:
            yield []
        else:
            for item in self.solution_1269_3_2(seq[1:]):
                yield [seq[0]]+item
                yield item
    def solution_1269_3_3(self, nums: List[int]) -> int:
        lis = [x for x in self.solution_1269_3_2(nums)]
        sumXor = 0
        lis.sort()
        #print(lis)
        for i in lis:
            sumXor += self.solution_1269_3_1(i)
        return sumXor