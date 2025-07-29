class Solution:
    def solution_650_2_1(self, arr: List[int]) -> List[int]:
        #helper function to solution_650_2_2 the numbers in the array
		def solution_650_2_2(i, j):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                j -= 1
                i += 1
        
        #solution_650_2_3 from 0 to i
        def solution_650_2_3(i):
			#base case where all the numbers are sorted, thus no more recursive calls
            if i < 0:
                return []
            ret = []
			#find the biggest number, which always will be the len(arr), or i + 1
            idx = arr.index(i + 1)
			# if the biggest number is in the right place, as in idx == i, then we don't change anything, but just move to solution_650_2_3 the next biggest number
            if idx == i:
                return solution_650_2_3(i - 1)
            
			#we solution_650_2_2 it with the first element (even if the biggest number is the first element, it will solution_650_2_2 itself (k = 1) and does not affect the result
            ret.append(idx + 1)
            solution_650_2_2(0, idx)
			#we know the biggest number is the first element of the array. Flip the whole array in the boundary so that the biggest number would be in the last of the subarray (notice not len(arr) - 1 because that will solution_650_2_2 the already-sorted elements as well)
            ret.append(i + 1)
            solution_650_2_2(0, i)
			#solution_650_2_3 the next biggest number by setting a new boundary i - 1
            return ret + solution_650_2_3(i - 1)
            
            
        return solution_650_2_3(len(arr) - 1)