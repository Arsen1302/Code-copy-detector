class Solution(object):
    def solution_1033_4(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
		#initialise a variable to store the output
        result = 0
		#loop through each each index untill except the last 2 as we are looking for set of 3 numbers
        for i in range(len(arr)-2):
		#loop from 2nd element to the 2nd last element
            for j in range(1,len(arr)-1):
			#This condition is reduce excessive computation as we dont want to deal with j<=i
                if j<=i:
                    continue
					#loop from 3rd element to end of the list
                for k in range(2,len(arr)):
				#This condition is to remove excess computation as we dont want to deal with k<=j
                    if k<=j:
                        continue
						#Checking whether the condition given in the question is being satisfied
                    if ((abs(arr[i] - arr[j]) <= a) and (abs(arr[j] - arr[k]) <= b) and abs(arr[i] - arr[k]) <= c):
					#increment the output variable whenever we find a suitable pair (i,j,k) that satisfies all the conditions
                        result+=1
        return result