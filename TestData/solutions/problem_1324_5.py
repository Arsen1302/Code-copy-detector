class Solution:
    def solution_1324_5(self, times: List[List[int]], targetFriend: int) -> int:
        n, d = len(times), dict()
        heap = [i for i in range(n)]
        cur = []
        for i, (s, e) in enumerate(times):
            cur += [(s, i), (-e, i)]
        for idx, friend in sorted(cur, key=lambda x: (abs(x[0]), x[0])):
            if idx > 0:
                d[friend] = heapq.heappop(heap)
                if friend == targetFriend: return d[friend]
            else:    
                heapq.heappush(heap, d[friend])
        return -1