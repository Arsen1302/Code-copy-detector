class Solution:
    def solution_1390_2(self, grid: List[List[int]], x: int) -> int:
        li = []
        
        # convert matrix to array, we dont care about the structure itself. We just want the values
        for val in grid:
            li+= val
        
        # sort the array
        li.sort()
        
        # get the middle value, which is equidistant from both sides
        median = li[len(li)//2]
        ops = 0
        
        # run the loop over all the elements to calculate the number of operations needed
        for val in li:
            
            # this is the condtion which determines if our number can reach the other number with adding/subtracting k
            if abs(val-median)%x != 0:
                return -1
            ops += abs(val-median)//x
        return ops