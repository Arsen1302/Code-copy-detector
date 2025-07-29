class Solution:
    def solution_1198_4_1(self, groups: List[List[int]], nums: List[int]) -> bool:
        grouplen = len(groups)
        numslen = len(nums)
        @lru_cache(None)
        def solution_1198_4_2(groupindex, innerindex, cont ,numsindex):
            if groupindex == grouplen:
                return True
            if numsindex == numslen:
                return False
            # we match
            ok = False
            if groups[groupindex][innerindex] == nums[numsindex]:
                if innerindex == len(groups[groupindex]) - 1:
                    ok |= solution_1198_4_2(groupindex + 1, 0, 1 ,numsindex + 1)
                else:
                    ok |= solution_1198_4_2(groupindex, innerindex + 1, 1 ,numsindex + 1)
            # we don't match
            ok |= solution_1198_4_2(groupindex, 0, 0 ,numsindex + 1)
            return ok
        return solution_1198_4_2(0,0,0,0)