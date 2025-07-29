class Solution:
	def solution_1328_3(self, num: str, change: List[int]) -> str:
		temp = int(num)
		num = list(num)
		flag = True
		for i,k in enumerate(num):
			if int(k) == int(change[int(k)]):
				continue
			elif int(k) < int(change[int(k)]):
				num[i] = str(change[int(k)])
				flag = False
			elif flag == False:
				return ''.join(num)
		return ''.join(num)