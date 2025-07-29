class Solution:
    def solution_1397_4(self, nums: List[int]) -> int:
        ans = {}
        subSet = [[]]
        max_or = 0
        for i in range(len(nums)):
            for j in range(len(subSet)):
                new = [nums[i]] + subSet[j]
                # print(new)
                x = new[0]
                for k in range(1, len(new)):
                    x |= new[k]
                x = max(max_or, x)
                if x in ans:
                    ans[x] += 1
                else:
                    ans[x] = 1
                subSet.append(new)
        return ans[x]