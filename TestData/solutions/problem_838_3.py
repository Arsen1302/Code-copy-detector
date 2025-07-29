class Solution:
    def solution_838_3(self, groupSizes: List[int]) -> List[List[int]]:
        res = []
        groups = collections.defaultdict(list)

        for i, size in enumerate(groupSizes):
            groups[size].append(i)
            if len(groups[size]) == size:
                res.append(groups[size])
                groups[size] = []
        
        return res