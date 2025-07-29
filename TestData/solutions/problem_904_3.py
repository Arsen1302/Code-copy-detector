class Solution:
	def solution_904_3(self, digits: List[int]) -> str:
		digits.sort()
		q0,q1,q2=[],[],[]
		sums=0
		for i in range(len(digits)):
			sums+=digits[i]
			remain=digits[i]%3
			if remain==0:
				q0.append(digits[i])
			elif remain==1:
				q1.append(digits[i])
			else:
				q2.append(digits[i])
		q1.sort(reverse=True)
		q2.sort(reverse=True)
		if sums%3==1:
			if q1:
				q1.pop()
			else:
				if q2:
					q2.pop()
				else:
					return ""

				if q2:
					q2.pop()
				else:
					return ""

		elif sums%3==2:
			if q2:
				q2.pop()
			else:
				if q1:
					q1.pop()
				else:
					return ""

				if q1:
					q1.pop()
				else:
					return ""

		res=q0+q1+q2
		res.sort(reverse=True)
		ans=""
		for i in res:
			ans+=str(i)
		return str(int(ans)) if ans else ans