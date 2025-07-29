class Solution:
    def solution_1454_3(self, arr: List[int]) -> List[int]:
	"""
	The key fact is that
	result[i] = sum(i - indices below i) + sum(indices above i - i)
	This implies
	results[i] = sum(indices above i) - sum(indices below i) + 
		i * (number of indices above i - number of indices below i)
	Fortunately, you can update the sums in constant time.
	"""
        indicesAbove = {}
        indicesBelow = {}
        runningSumAbove = {}
        runningSumBelow = {}
        result = [0] * len(arr)
        for i, n in enumerate(arr):
            if n not in indicesAbove:
                indicesAbove[n] = 1
                indicesBelow[n] = 0
                runningSumAbove[n] = i
                runningSumBelow[n] = 0
            else:
                indicesAbove[n] += 1
                runningSumAbove[n] += i
        # result = sum of numbers above - sum of #s below + pivot * (Nb - Na)
        for i, n in enumerate(arr):
            runningSumAbove[n] -= i
            indicesAbove[n] -= 1
            result[i] = runningSumAbove[n] - runningSumBelow[n] + i * (indicesBelow[n] - indicesAbove[n])
            indicesBelow[n] += 1
            runningSumBelow[n] += i
            
            
        return result
		```