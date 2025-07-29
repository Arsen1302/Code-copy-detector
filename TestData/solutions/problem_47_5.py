class Solution:
		def solution_47_5(self, gas: List[int], cost: List[int]) -> int:
			if sum(gas) < sum(cost):
				return -1
			fuel, strt_point = 0, 0
			for i in range(len(gas)):
				fuel += gas[i]-cost[i]
				if fuel < 0:
					strt_point = i+1
					fuel = 0
			return strt_point