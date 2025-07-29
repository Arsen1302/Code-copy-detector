class Solution:
    def solution_756_4(self, arr1: List[int], arr2: List[int]) -> List[int]:
        #Start with creating an array/list to store answer
        ans = []
        
        #Create a hashmap and store all the elements as key and their frequency as value
        mapD = {}
        
        for i in arr1:
            #map.get(i, 0) to avoid key error in hashmap/dictionary
            mapD[i] = 1 + mapD.get(i, 0)
            
        #update the answer with elements as their frequncy in arr1 but in the sequence of arr2
        for i in arr2:
            ans[:] += [i] * mapD[i]
        
        #create another hashmap and a temporary list to find and store all elements that are not in arr2
        h = {}
        li = []
        
        for i in arr1:
            h[i] = 1 + h.get(i, 0)
        
        #Update the temporary list with elements and their frequency which are distinct in arr1
        for i in h:
            if i not in arr2:
                li[:] += [i] * h[i]
           
        li.sort()
        
        #merge the both arrays and here is the final ans
        ans[:] += li[:]
        
        return ans