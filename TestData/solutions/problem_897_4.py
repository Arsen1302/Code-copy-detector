class Solution:
    def solution_897_4(self, target: List[int]) -> bool:
        heap = list(map(lambda x: -x,target))
        heapq.heapify(heap)
        summ = sum(heap)
        while True:
            item = heapq.heappop(heap)
            if item == -1: return True
            summ-=item
            if item >= summ or summ == 0: return False
            item = item % summ if item % summ else summ
            if item > -1:
                return False
            heapq.heappush(heap,item)
            summ+=item