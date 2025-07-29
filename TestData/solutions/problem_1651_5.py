class Solution:
    def solution_1651_5(self, nums: List[int], queries: List[int]) -> List[int]:
        
        ans = []

        nums.sort()
        sumx = []
        res = 0
        for x in nums:
            res += x
            sumx.append(res)

        for j in range(len(queries)):
            for i, y in enumerate(sumx):
                if y <= queries[j]:
                    continue
                else:
                    ans.append(i)
                    break
            else:
                if len(ans) < j + 1:
                    ans.append(len(nums))
        
        return ans