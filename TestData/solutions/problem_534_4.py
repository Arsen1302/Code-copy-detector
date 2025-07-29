class Solution:
    def solution_534_4(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand)%groupSize !=0 :return False
        
        queue=deque()
        
        heapify(hand)
        
        while hand:
            if not queue:
                queue.append([heappop(hand)])
            elif len(queue[-1])==groupSize:
                queue.pop()
            else:
                pop=heappop(hand)
                if pop == queue[-1][-1] and pop==queue[0][-1]: queue.append([pop])

                elif pop-queue[0][-1] > 1: return False

                else:
                    left=queue.popleft()
                    left.append(pop)
                    queue.append(left)
            

        return True if queue and len(queue[-1])==groupSize else False