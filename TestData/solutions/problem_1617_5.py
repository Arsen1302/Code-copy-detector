class Solution:
    def solution_1617_5(self, nums: List[int]) -> List[int]:
        hash_map=Counter(nums)
        count=0
        for i in hash_map:
            count+=hash_map[i]%2
        return [(len(nums)-count)//2,count]