class Solution:
    def solution_1353_1(self, nums: List[str]) -> str:
        return list(set(list((map(lambda x:"".join(list(map(str,x))),list(itertools.product([0,1],repeat=len(nums)))))))-set(nums))[0]