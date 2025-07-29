class Solution:
    def solution_1496_3(self, finalSum: int) -> List[int]:
        if(finalSum%2 != 0):
            return []
        
        finalSum = finalSum//2
        result = []
        total = 0
        remove = None
        for i in range(1, finalSum+1):
            result.append(i)
            total += i
            if(total == finalSum):
                break
            elif(total > finalSum):
                remove = total-finalSum
                break
        
        output = []
        for num in result:
            if(remove==None):
                output.append(2*num)
            else:
                if(num!=remove):
                    output.append(2*num)
        
        return output