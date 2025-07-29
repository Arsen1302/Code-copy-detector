class Solution:
    def solution_143_2(self, pattern: str, s: str) -> bool:
        
        #i/p : pattern = "abba" and s = "dog cat cat dog"
        
        arr1 = list(pattern) #arr1 = ["a", "b", "b", "a"] 
        arr2 = s.split() #arr2 = ["dog", "cat", "cat", "dog"]
        n = len(arr2) #len(arr1) == len(arr2) in all cases where True is possible 
        
        if len(arr1) != len(arr2): #we will never be able to map all characters 
            return False
        
        d1 = {} #to handle character mapping from arr1 to arr2 
        d2 = {} #to handle character mapping from arr2 to arr1
        
        #Below is our character mapping logic
        
        for i in range(0, n):
            
            if arr1[i] in d1 and d1[arr1[i]] != arr2[i]:
                return False
            
            if arr2[i] in d2 and d2[arr2[i]] != arr1[i]:
                return False
            
            d1[arr1[i]] = arr2[i] #after all loops : d1 = {"a" : "dog", "b" : "cat"}
            d2[arr2[i]] = arr1[i] #after all loops : d2 = {"dog" : "a", "cat" : "b"}
        
		#if none of the above condition returns False
		#it means that all characters of arr1 can be legally mapped to arr2, so, return True
        return True