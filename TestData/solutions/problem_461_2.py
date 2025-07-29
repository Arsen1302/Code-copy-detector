class Solution:
    def solution_461_2(self, S: str) -> str:
        if not S: return ''
        heap, last, ans = [], None, ''
        counts = collections.Counter(S)
        for ch in counts:
            heapq.heappush(heap, (-counts[ch], ch))
            
        while heap:
            count, ch = heapq.heappop(heap)
            ans += ch
            if last:
                heapq.heappush(heap, last)
            last = (count+1, ch) if count != -1 else None
        return ans if not last else ''