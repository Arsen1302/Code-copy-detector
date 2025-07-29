class Solution:
	def solution_218_3_1(self):
		self.visited=dict()
		self.length=0
		self.width=0

	def solution_218_3_2(self, minPriorityQueue, value):
		length=len(minPriorityQueue)
		start=0
		end=length-1
		while start<=end:
			mid=(start+end)//2
			if minPriorityQueue[mid][0]>value[0]:
				end=mid-1
			else:
				start=mid+1
		if start>end:
			minPriorityQueue.insert(start, value)
		return minPriorityQueue

	def solution_218_3_3(self, coor):
		neighbours=[]
		if coor[0]+1<=self.length-1 and not self.visited[coor[0]+1][coor[1]]:
			neighbours.append([coor[0]+1, coor[1]])
		if coor[0]-1>=0 and not self.visited[coor[0]-1][coor[1]]:
			neighbours.append([coor[0]-1, coor[1]])
		if coor[1]+1<=self.width-1 and not self.visited[coor[0]][coor[1]+1]:
			neighbours.append([coor[0], coor[1]+1])
		if coor[1]-1>=0 and not self.visited[coor[0]][coor[1]-1]:
			neighbours.append([coor[0], coor[1]-1])
		return neighbours

	def solution_218_3_4(self, heightMap: List[List[int]]) -> int:
		self.length=len(heightMap)
		self.width=len(heightMap[0])

		minPriorityQueue=[]

		row=0
		while row<self.length:
			col=0
			while col<self.width:
				if (row==0 or row==self.length-1 or col==0 or col==self.width-1):
					minPriorityQueue=self.solution_218_3_2(minPriorityQueue, [heightMap[row][col], row, col])
					try:
						self.visited[row].update({col: True})
					except:
						self.visited[row]={col: True}
				else:
					try:
						self.visited[row].update({col: False})
					except:
						self.visited[row]={col: False}
				col+=1
			row+=1

		storage=0
		currentMinimumHeight=0

		while len(minPriorityQueue)>0:
			coor=minPriorityQueue.pop(0)[1:]
			currentMinimumHeight=max(currentMinimumHeight, heightMap[coor[0]][coor[1]])
			neighbours=self.solution_218_3_3(coor)

			for neighbour in neighbours:
				currentHeight=heightMap[neighbour[0]][neighbour[1]]
				if currentHeight<currentMinimumHeight:
					storage+=(currentMinimumHeight-currentHeight)

				minPriorityQueue=self.solution_218_3_2(minPriorityQueue, [heightMap[neighbour[0]][neighbour[1]], neighbour[0], neighbour[1]])
				self.visited[neighbour[0]][neighbour[1]]=True

		return storage