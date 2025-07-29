class Solution:
    def solution_269_5(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        max_r = 0
        heater = 0
        
        for i,house in enumerate(houses):
            # Greedy: check if the next heater will shorter the radius compared to the current one
            # it will always improve the max_r as the later index houses will stay on the RHS of current house
			# and if the next heater will reduce the radius, therefore next heater will also reduce  the radius for later house
            while heater + 1 < len(heaters) and abs(heaters[heater] - house) >= abs(heaters[heater+1] - house):
                heater+=1
            max_r = max(max_r, abs(heaters[heater] - house))
        return max_r