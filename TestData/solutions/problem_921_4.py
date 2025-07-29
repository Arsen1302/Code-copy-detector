class Solution:
	def solution_921_4(self, arr1: List[int], arr2: List[int], d: int) -> int:
		s=0
		for i in arr1:
			t=0
			for j in arr2:
				if abs(i-j)<= d:
					t=1
					break
			if t==0:
				s=s+1
		return s