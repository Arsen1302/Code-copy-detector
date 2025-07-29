class Solution:
    def solution_1247_1(self, costs: List[int], coins: int) -> int:
        '''
        1. If the minimum of all costs is greater than amount of coins, the boy can't buy any bar, return 0
        2. Else, sort the list of costs in a non-decreasing order
        3. For each 'cost' in costs, if the cost is less than current coins
                -increase the count of ice cream bars that can be bought by 1
                -decrease the current coins amount by 'cost'
        4. If the cost is greater than current coins, return the ice cream bar count value
        '''
        
        if min(costs)>coins:        #minimum cost is greater than the coins available        
            return 0                #can't buy any ice cream bar
        
        costs=sorted(costs)         #sort the list of costs in a non-decreasing order
        res = 0                     #the resultant count of ice cream bars that can be bought
        for cost in costs:
            if cost<=coins:         #in this case, the boy can buy the ice cream bar
                res+=1              #increase the ice cream bar count
                coins-=cost         #spent an amount equal to 'cost', decrease current coins amount by cost
            else:
                break               #not enough coins, return the bars count
            
        return res