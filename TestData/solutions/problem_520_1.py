class Solution:
    def solution_520_1(self, image: List[List[int]]) -> List[List[int]]:
        """
        Simple &amp; striaghtforward without using inbuilt functions.
     
        In actual the run time is very less as we are iterating only n/2 time
        for each image list.
        Time complexity : O(n * n/2) == O(n^2) 
        Space complexity : O(1)
        """
        
        for im in image: #Iterate through each im list in the image list.
            i, j = 0, len(im)-1    #Maintain two pointers one at start and one at end.
            while i <= j:          #Iterate while first pointer is less than or equal to second pointer.
                im[i], im[j] = im[j]^1, im[i]^1   #swap element at both pointer &amp; complement them at the same time.
                i +=1              #increment first pointer to move forward
                j -=1              #decrement second pointer to move backward
            
        return image         # return same list
    
    
        """
        Using inbuilt functions
        """
        # for im in range(len(image)):
        #     image[im] = list(map(lambda a : abs(a-1), reversed(image[im])))
        # return image
    
        """
        One liner
        """
        return [[i^1 for i in im[::-1]] for im in image]