class Solution:
    def solution_1249_3(self, arr1: List[int], arr2: List[int]) -> int:
        
        # GET MIN LOOP LENGTH
        length = min(len(arr1), len(arr2))
        
        # Break into 2 sets
        a1 = 0
        b1 = 0
        
        # SHORT CUT IF THEY ARE THE SAME LENGTH
        if len(arr1) == len(arr2):
            while len(arr1):
                a1 ^= arr1.pop()
                b1 ^= arr2.pop()
                
            return (b1 &amp; a1)
        
        # IF YOU MADE IT THIS FAR THE ARRAYS ARE UNEVEN
        for idx in range(length):
            a1 ^= arr1.pop()
            b1 ^= arr2.pop()
            
        # IF ARRAY 1 IS LARGER RUN THROUGH THEM
        if len(arr1) > 0:
            while len(arr1):
                a1 ^= arr1.pop()
                
        if len(arr2) > 0:
            while len(arr2):
                b1 ^= arr2.pop()
            
        return (a1 &amp; b1)