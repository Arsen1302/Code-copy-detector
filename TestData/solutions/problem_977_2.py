class Solution:
    def solution_977_2(self, s: str, k: int) -> int:
        
        n = len(s)
       
        #STEP 1
        arr = []
        for i in range(0, n):
                arr.append(s[i : i + k])
        
        vowels = ["a", "e", "i", "o", "u"]
        arr1 = []
        
		#STEP 2
        for i in arr:
            count = 0 
            if len(i) == k:
                for j in i:
                    if j in vowels:
                        count += 1 
                arr1.append(count)
        
		#STEP 3
        if len(arr1) != 0:
            value = max(arr1)
            return value
        else:
            return 0