class Solution:
    def solution_251_4(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0])            # sorting so that you always get the next closest start point of balloons
        end = float('inf')                           # This end constraint will ensure that the overlapping balloon can be hit with single arrow 
		res = 1                                      # I initialized res with 1 since we are given in constraint that min length of points is 1 so 1 arrow would always be the base case
        for p in points:                             # Traversing the points array once  
            if p[0] <= end:                          # p[0] means the starting point. If this is less than or equal to our end constraint, that means that this ballon can be shot with the current arrow.
                end = min(end, p[1])                 # The end constraint for the current arrow would always be the min of all the end points we have encountered for the current arrow
            else:
                end = p[1]                           # If the start is after the end constraint, The iteration for the current arrow is over. 
                res += 1                              # We can say here, we released our current arrow and loaded a new one
        return res
		```