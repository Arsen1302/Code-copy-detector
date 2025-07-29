class Solution:
    def solution_461_5(self, s: str) -> str:
        last, amountLast = None, None
        count = Counter(s)
        maxHeap = [(-count[char], char) for char in count.keys()]
        heapq.heapify(maxHeap)
        res = ""
        while maxHeap:
            tmp = heapq.heappop(maxHeap)
            res += tmp[1]
            
            if amountLast:
                heapq.heappush(maxHeap, (amountLast, last))
            
            last, amountLast = tmp[1], tmp[0] + 1
        return res if len(res) == len(s) else ""