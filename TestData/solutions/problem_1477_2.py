class Solution:
    def solution_1477_2(self, nums: List[int]) -> List[int]:
        ans, positives, negatives = [], [], []
        for val in nums:
            if val >= 0:
                positives.append(val)
            else:
                negatives.append(val)
        for i in range(len(positives)):
            ans.append(positives[i])
            ans.append(negatives[i])
        return ans