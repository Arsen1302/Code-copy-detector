class Solution:
    def solution_1477_5(self, nums: List[int]) -> List[int]:
        positives = [num for num in nums if num > 0]
        negatives = [num for num in nums if num < 0]
        
        res = zip(positives, negatives)
        
        return chain(*res)