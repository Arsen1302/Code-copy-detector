class Solution:
    def solution_337_4_1(self, nums: List[int]) -> int:
        def solution_337_4_2(node):
            visited.add(node)
            this_group.add(node)
            neigh = nums[node]
            if neigh not in visited:
                solution_337_4_2(neigh)
        
        ans = 0
        visited = set()
        for node in range(len(nums)):
            if node not in visited:
                this_group = set()
                solution_337_4_2(node)
                ans = max(ans, len(this_group))
        return ans