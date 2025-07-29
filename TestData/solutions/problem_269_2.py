class Solution:
    def solution_269_2(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        res = 0
        heater = 0
        
        for h in houses:
            while heater + 1 < len(heaters) and heaters[heater + 1] == heaters[heater]:                  # Avoid duplicates
                heater += 1
            while heater + 1 < len(heaters) and abs(heaters[heater + 1] - h) < abs(heaters[heater] - h): # If using next heater is more efficient
                heater += 1                                                                              # Then use next heater
            
            res = max(res, abs(heaters[heater] - h))        # Update its range to house
        
        return res