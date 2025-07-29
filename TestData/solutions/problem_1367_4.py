class Solution:
	def solution_1367_4(self, rectangles: List[List[int]]) -> int:
		for i in range(0,len(rectangles)):
			r=rectangles[i][1]/rectangles[i][0]
			rectangles[i]=r

		count=0
		for j in range(0,len(rectangles)-1):
			Slice=rectangles[j+1:]
			c=Slice.count(rectangles[j])
			count=count+c
		return count