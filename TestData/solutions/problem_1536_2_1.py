class Solution:
    def solution_1536_2_1(self, num: int) -> int:
        oddHeap = []
        evenHeap = []
        evenParity = []
        
        while num>0:
            rem = num % 10
            num = num // 10
            if rem%2 == 0:
                heapq.heappush(evenHeap, -rem)
                evenParity.append(True)
            else:
                heapq.heappush(oddHeap, -rem)
                evenParity.append(False)
                
        return self.solution_1536_2_2(evenHeap, oddHeap, reversed(evenParity))
        
    def solution_1536_2_2(self, evenHeap, oddHeap, evenParity):
        result = 0
        for parity in evenParity:        
            if parity:
                result = result * 10 + (-heapq.heappop(evenHeap))
            else:
                result = result * 10 + (-heapq.heappop(oddHeap))
        return result