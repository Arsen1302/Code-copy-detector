class Solution:
    def solution_990_2(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:        
        # dp_values[i][j][k] records the min costs that we have k+1 neighbors 
        # in the first i houses and the ith house is painted with j
        dp_values = [[[float('inf')]*target for _ in range(n)] for _ in range(m)]
		# initial values
        if houses[0] != 0:
            dp_values[0][houses[0]-1][0] = 0
        else:
            for i in range(n):
                dp_values[0][i][0] = cost[0][i]
        for i in range(1, m):
            for j in range(n):
                # houses[i] is painted. we only consider when j == houses[i]
                if houses[i] != 0 and j != houses[i]-1:
                    continue
                for k in range(target):
                    # for i houses, we can't have more than i neighbors 
                    if k > i:
                        break
                    if houses[i-1] != 0:
                        if j == houses[i-1]-1:
                            dp_values[i][j][k] = dp_values[i-1][j][k]
                        else:
                            # if k == 0, it makes no sense to consider the case that current 
                            # house color is different from the previous house's color.
                            if k > 0:
                                dp_values[i][j][k] = dp_values[i-1][houses[i-1]-1][k-1]
                    else:
                        min_with_diff_color = float('inf')
                        if k > 0:
                            for w in range(n):
                                if w == j:
                                    continue
                                min_with_diff_color = min(min_with_diff_color, dp_values[i-1][w][k-1])
                        dp_values[i][j][k] = min(min_with_diff_color, dp_values[i-1][j][k])
                    # if the house is not painted, we need extra cost
                    if houses[i] == 0:
                        dp_values[i][j][k] += cost[i][j]
        costs = float('inf')
        for j in range(n):
            costs = min(costs, dp_values[m-1][j][target-1])
        return costs if costs != float('inf') else -1