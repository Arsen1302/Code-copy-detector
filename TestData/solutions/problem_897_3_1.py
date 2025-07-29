class Solution:
    def solution_897_3_1(self, target: List[int], targetTotal: int) -> bool:
        while 1:
            if targetTotal == len(target): # All elements must be 1
                return True
            if targetTotal < len(target): # One element must be < 1
                return False

            # Can I reach a collection where we have every number but the maximum one
            # and the sum total of the existing numbers will be same as the maximum?
            # The means I need to get to an array where we have all the numbers except
            # for the max one and a different number n' that is smaller than max.
            maxNo = target[0] * (-1)
            totalExcludingMax  = targetTotal - maxNo
            if totalExcludingMax == 0:
                # this is possible only when the array contains only one element
                # if that element is 1 then that condition is already covered.
                return False
            # nPrime             = maxNo - totalExcludingMax
            # If nPrime still remains max then we'll subtract totalExcludingMax from it
            # and we'll continue doing it either until it becomes negative or < next max
            # number in the array. That may happen only when at least
            # nPrime is < totalExcludingMax. This number can be achieved as
            # nPrime = maxNo % totalExcludingMax.
            # At this nPrime may still be bigger than the next max number. If that
            # condition happens then nPrime will become negative in the next run and
            # the loop will end with a failure.
            if totalExcludingMax >= maxNo:
                return False # We cannot end up with a number < 1
            nPrime = maxNo % totalExcludingMax
            if nPrime < 1:
                nPrime += totalExcludingMax # Only subtract until it stays positive
            
            heapq.heapreplace(target, -1 * nPrime)
            targetTotal = totalExcludingMax + nPrime # maxNo should be the previous target
    
    def solution_897_3_2(self, target: List[int]) -> bool:
        targetHeap = [-1 * k for k in target] # Order doesn't matter
                                              # If generation is possible then it is possible
                                              # irrespective of the orders
        #print(target)
        heapq.heapify(targetHeap)
        #print(target)
        
        return self.solution_897_3_1(targetHeap, sum(target))