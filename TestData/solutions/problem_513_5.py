class Solution:
    def solution_513_5(self, ages: List[int]) -> int:
        deque = collections.deque()
        ages.sort(reverse=True)
        res = 0
        curSame = 0
        
        for i, age in enumerate(ages):
            if i and age >= 15 and age == ages[i-1]:
                curSame += 1
            else:
                curSame = 0

            while deque and age <= deque[0]:
                deque.popleft()
                
            res += len(deque) + curSame
            deque.append(0.5*age + 7)
        
        return res