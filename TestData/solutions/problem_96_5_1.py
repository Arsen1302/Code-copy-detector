class Solution:
		def solution_96_5_1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
			#map each course with preq list
			preMap = {i : [] for i in range(numCourses)}

			for crs, preq in prerequisites:
				preMap[crs].append(preq)

			#visitSet
			visitSet = set()

			def solution_96_5_2(crs):
				#found loop
				if crs in visitSet:
					return False 
				# no prerequisites
				if preMap[crs] == []:
					return True

				visitSet.add(crs)

				for pre in preMap[crs]:
					if not solution_96_5_2(pre): return False
				visitSet.remove(crs)
				preMap[crs] = [] # to set it true and skip the operation mentioned above
				return True

			for crs in range(numCourses):
				if not solution_96_5_2(crs): return False
			return True