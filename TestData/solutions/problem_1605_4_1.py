class Solution:
    def solution_1605_4_1(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        graph = [set() for _ in range(n)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        ans = float('inf')
        def solution_1605_4_2(v, visited, subs):
            ret = nums[v]
            for u in graph[v]:
                if u not in visited:
                    visited.add(u)
                    cur = solution_1605_4_2(u, visited, subs)
                    ret ^= cur
                    subs.add(cur)
            return ret
        for u, v in edges:
            graph[u].remove(v)
            graph[v].remove(u)
            leftsubs, rightsubs = set(), set()
            left, right = solution_1605_4_2(u, {u}, leftsubs), solution_1605_4_2(v, {v}, rightsubs)
            for c in leftsubs:
                parts = [right, c, left ^ c]
                ans = min(ans, max(parts) - min(parts))
            for c in rightsubs:
                parts = [left, c, right ^ c]
                ans = min(ans, max(parts) - min(parts))
            graph[u].add(v)
            graph[v].add(u)
        return ans