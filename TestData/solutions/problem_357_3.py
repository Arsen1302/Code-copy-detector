class Solution:
	def solution_357_3(self, paths: List[str]) -> List[List[str]]:

		result = []

		directory = {}

		for path in paths:

			path = path.split()

			dir_name = path[0]

			for file in path[1:]:

				start_index = file.index('(')
				end_index = file.index(')')

				content = file[start_index + 1 : end_index ]

				if content not in directory:

					directory[content] =  [dir_name + '/' + file[ : start_index]]
				else:
					directory[content].append(dir_name + '/' + file[ : start_index])


		for key in directory:

			if len(directory[key]) > 1:
				result.append(directory[key])

		return result