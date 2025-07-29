class Solution:
    def solution_838_5(self, groupSizes: List[int]) -> List[List[int]]:
        ids = dict() #mapping from size to ids
        for i, size in enumerate(groupSizes): 
            ids.setdefault(size, []).append(i)
        ans = []
        for size, ids in ids.items():
            ans.extend([ids[i:i+size] for i in range(0, len(ids), size)]) #split list into list of list
        return ans