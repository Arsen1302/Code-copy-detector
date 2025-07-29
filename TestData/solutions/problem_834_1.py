class Solution:
    def solution_834_1(self, tomatoSlices, cheeseSlices):
		# on the basis of the matrix solution
        ans = [0.5 * tomatoSlices - cheeseSlices, -0.5 * tomatoSlices + 2 * cheeseSlices]
		
		# using the constraints to see if solution satisfies it
        if 0 <= int(ans[0]) == ans[0] and 0 <= int(ans[1]) == ans[1]:
            return [int(ans[0]), int(ans[1])]
        else:
            return []