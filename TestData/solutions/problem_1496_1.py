class Solution:
    def solution_1496_1(self, finalSum: int) -> List[int]:
        l=set()
        if finalSum%2!=0:
            return l
        else:
            s=0
            i=2                       # even pointer 2, 4, 6, 8, 10, 12...........
            while(s<finalSum):
                s+=i                #sum 
                l.add(i)      # append the i in list
                i+=2
            if s==finalSum:  #if sum s is equal to finalSum then no modidfication required
                return l
            else:
                l.discard(s-finalSum)  #Deleting the element which makes s greater than finalSum
				return l