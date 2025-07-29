class Solution:
    def solution_663_1(self, days: List[int], costs: List[int]) -> int:
		#create the total costs for the days 
        costForDays = [0 for _ in range(days[-1] + 1) ]
		#since days are sorted in ascending order, we only need the index of the days we haven't visited yet
        curIdx = 0
		
        for d in range(1, len(costForDays)):
			#if we do not need to travel that day
			#we don't need to add extra costs
            if d < days[curIdx]:
                costForDays[d] = costForDays[d - 1]
                continue
            
			#else this means we need to travel this day
			#find the cost if we were to buy a 1-day pass, 7-day pass and 30-day pass
            costs_extra_1 = costForDays[d - 1] + costs[0]
            costs_extra_7 = costForDays[max(0, d - 7)] + costs[1] 
            costs_extra_30 = costForDays[max(0, d - 30)] + costs[2]
            
			#get the minimum value
            costForDays[d] = min(costs_extra_1, costs_extra_7, costs_extra_30)
			
			#update the index to the next day we need to travel
            curIdx += 1
			
        return costForDays[-1]