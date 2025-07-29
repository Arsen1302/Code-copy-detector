class Solution:
    
    def solution_283_4_1(self, arr: List[int]) -> int:
        count = 0
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]
            count = self.solution_283_4_1(L) 
            count += self.solution_283_4_1(R)
            count += self.solution_283_4_2(L,R,arr)
        return count
    
    def solution_283_4_2(self,L,R,arr):
		#finding count for the condition
        count = 0
        i,j = 0,0
        while i < len(L):
            while j < len(R):
                if L[i] > 2*R[j]:
                    j += 1
                else:
                    break
            
            if j > 0:
                count += j
            i += 1

		#merging the sorted arrays
        i,j,k = 0,0,0        
        while i < len(L) and j < len(R):    
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1   
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            k += 1
            i += 1   
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
                
        return count