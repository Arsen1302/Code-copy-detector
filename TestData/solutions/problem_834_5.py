class Solution:
    def solution_834_5(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices%2:
            return []
        x=tomatoSlices//2
        diff=x-cheeseSlices
        if diff<0:
            return []
        if x-(2*diff)<0:
            return []

        return [diff,x-(2*diff)]


#     Logic is if tomatoslice is odd, not any combination possible return []
#     x is total no. of smallburgers possible
#     diff is difference in no. of cheeseSlices,it also represent no. of jumboburgers 
#     if diff<0 , means even combinations of smallburgers can't fullfill all the slices
#     so return []
#     return [diff,x-(2*diff)]