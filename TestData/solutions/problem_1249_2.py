class Solution:
    def solution_1249_2(self, arr1: List[int], arr2: List[int]) -> int:
        '''
        1. According to the hints, XORSum = (XORSum of arr1) bitwise AND (XORSum of arr2)
        2. Calculate the XOR Sums of arr1 and arr2 separately and store them in separate variables
        3. Perform bitwise AND on those XOR Sums
        '''
        
        xor1 = arr1[0]                      #at first store the first element as the XOR sum of arr1
        xor2 = arr2[0]                      #at first store the first element as the XOR sum of arr2
        
        if len(arr1)>=2:
            for i in range(1,len(arr1)):    
                xor1^=arr1[i]               #iteratively XOR with the next element
            
        if len(arr2)>=2:
            for i in range(1,len(arr2)):
                xor2^=arr2[i]               #iteratively XOR with the next element
                
        return xor1&amp;xor2                    #bitwise AND of XORSum of arr1 and XORSum of arr2