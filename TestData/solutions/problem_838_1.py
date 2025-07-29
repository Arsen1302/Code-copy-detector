class Solution:
    # Time: O(n)
    # Space: O(n)
    def solution_838_1(self, groupSizes: List[int]) -> List[List[int]]:
        res, dic = [], {}
        for idx, group in enumerate(groupSizes):
            if group not in dic:
                dic[group] = [idx]
            else:
                dic[group].append(idx)
            
            if len(dic[group]) == group:
                res.append(dic[group])
                del dic[group]
        return res