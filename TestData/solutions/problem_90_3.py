class Solution:
    def solution_90_3(self, left: int, right: int) -> int:
        
        if left == 0 and right == 0:                    #To check if both inputs are 0
            return 0
        elif len(bin(left)) != len(bin(right)):        #To check if both inputs have unequal binary number length
            return 0
        else:                                                      
            left = bin(left)[2:]
            right = bin(right)[2:]
            for i in range(len(right)):
                if left[i] != right[i]:              #We need only the equal elements of left and right numbers; discard all elements after an unequal element
                    left = left[:i] + ("0" * len(right[i:]))        
                    break
            return int(left, 2)