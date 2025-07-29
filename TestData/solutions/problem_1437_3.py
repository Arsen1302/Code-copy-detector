class Solution:
    def solution_1437_3(self, nums: List[int], k: int) -> List[int]:
        valindex=sorted([(num,i) for i,num in enumerate(nums)],reverse=True)
        return [num for num,i in sorted(valindex[:k],key=lambda x:x[1])]