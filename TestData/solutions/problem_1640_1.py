class Solution:
    def solution_1640_1(self, edges: List[int]) -> int:

        n = len(edges)
        cnt = defaultdict(int)
        ans = 0
        
		// we have the key stores the node edges[i], and the value indicates the edge score.
        for i in range(n):
            cnt[edges[i]] += i

        m = max(cnt.values())

		// In the second iteration, i is also the index of the node. So the first one meets == m, is the smallest index.
        for i in range(n):
            if cnt[i] == m:
                ans = i
                break
        
        return ans