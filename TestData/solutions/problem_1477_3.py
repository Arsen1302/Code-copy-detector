class Solution:
    def solution_1477_3(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        ans = []
        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        for j in range(len(nums)//2):
            ans.append(pos[j])
            ans.append(neg[j])
        return ans