class Solution:
    def solution_663_3(self, days: List[int], costs: List[int]) -> int:
        # map the number of days per ticket to the cost
        cost_map = {
            1: costs[0],
            7: costs[1],
            30: costs[2],
        }
        
        travelling_days = set(days)  # set of active travel days
        dp_costs = [0 for x in range(days[-1] + 1)]  # tracks the min cost day
        
        for i in range(days[-1] + 1):
            # store most recent lowest sum in arr to use later
            if i not in travelling_days:
                dp_costs[i] = dp_costs[i - 1]
                continue
                
            possible_costs = []
            for ticket,cost in cost_map.items():
                day_diff = i - ticket
                
                if day_diff <= 0:
                    # this ticket will cover the total cost
                    possible_costs.append(cost)
                else:
                    # ticket was bought day_diff ago
                    # sum lowest cost on day_diff with new ticket cost
                    possible_costs.append(cost + dp_costs[day_diff])
            
            # find min of all ticket options on this day
            dp_costs[i] = min(possible_costs)
            
        return dp_costs[-1]