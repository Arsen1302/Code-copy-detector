class Solution:
    def solution_895_4(self, grid: List[List[int]]) -> int:

        #BINARY SEARCH  
        negative=0 #total negatives
        for i in grid: #traverse every row of grid
            l=0 #initial index of row
            h=len(i)-1 #last index of that row
            while l<=h: #traverse all indeces of any row
                mid=(l+h)//2 #middle index
                if i[mid]>=0: #if element is positive then no negative count
                    l=mid+1 #then check ->negative may be present after mid element
                else: 
                    #negative count-> from the element found negative,after that index 
                    #every element present in non-increasing sorted row will have negatives 
                    negative+=h-mid+1 
                    h=mid-1 #then check if negatives present before that mid element
        return negative