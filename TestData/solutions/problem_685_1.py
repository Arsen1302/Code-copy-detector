class Solution:
	def solution_685_1(self, A: List[int], K: int) -> int:
		A.sort()
		i = 0
		while i < len(A) and K>0:
			if A[i] < 0: # negative value
				A[i] = A[i] * -1 # update the list, change negative to positive
				K-=1

			elif A[i] > 0: # positive value
				if K % 2 == 0: # let K==2(must be even value), this means -1*-1==1 so it has no effect on sum
					return sum(A)
				else: return sum(A) - 2 * min(A) # let A==[1,2,3],K=1, so equation is 6-2(1)==4, same as -1+2+3=4 after taking the minimum in the list to give the largest possible sum required in the question

			else: return sum(A) # if A[i]==0,just sum cuz 0 is neutral: 1-0==1 or 1+0==1 thus no change just sum

			i+=1

		if K > len(A): # that means we have changed all values to positive
			A.sort() # cuz now its the opposite let A = [-4,-2,-3], K = 8, now flipping all negatives to positives, we have a new minimum which is 2
			if K % 2 == 0: # Here onwards is basically the same thing from before
				return sum(A)
			else: return sum(A) - 2 * min(A)

		return sum(A)