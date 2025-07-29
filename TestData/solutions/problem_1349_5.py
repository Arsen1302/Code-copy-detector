class Solution:
    def solution_1349_5(self, matrix: List[List[int]]) -> int:
        '''
        given : n*n matrix
        goal : maximize summation of all elements in matrix
        
        1. The max possible sum can be sum of all positive elements in matrix i.e when all are positive.
        2. Now suppose if there are even number of -ve elements then they can be all turned to positive numbers 
        and then again we can achieve the maximum result .
        eg : -1 2 1 -2
              3 1 -1 0
              1 -1 3 1
        see here even if all the negative elements are not adjacent to each other but it is given that
        we can perform this operation any number of times s
        
        so we can start with any one negative element keep multiplyting it with its adjacent element until 
        we reach a point where both the elements are -ve and after multiplying each of them by -1 we get positive
        numbers .
        
        3. if there are odd number of -ve elements then we need to get the minimum number (greater than
        0 .
        
        Note : One catch here is that we can treat 0s and use them to swap with negative elements 
        in this eg : 
        -3 0 0
        0 0 0
        0 3 2
        zero = 6
        neg = 1
        since here only one negative element is present we might end up thinking that we cant make this 
        to a positive number but instead we can make use of 0s . we ll use only that many number of zeros 
        such that the count of negative number becomes even.
             
        '''
        tot,min1,neg,zero = 0,sys.maxsize,0,0
        n = len(matrix)
        
        for i in range(n):
            for j in range(n):
                val = matrix[i][j]
                if val < 0:
                    neg += 1
                elif val == 0:
                    zero += 1
                    
                val = abs(matrix[i][j])
                tot += val
                if 0 < val < min1 :
                    min1 = val
                    
        while zero >=1 and neg%2 != 0:
            neg += 1
            zero -= 1
            
        if neg%2 != 0:
            return tot-(2*min1)
        return tot