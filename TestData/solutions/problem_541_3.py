class Solution:
    def solution_541_3(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # Init 
        fleets = 0
        fleet_time = float("-inf")
        
        # Cars which are ahead are checked first
        for pos, reach_time in sorted([(position[i], (target-position[i])/speed[i]) for i in range(len(position))], reverse=True):
            
            # If no collision, consider it a fleet. Read the comments.
            # If a car has higher reach time then the current fleet, that car
            # will never reach the fleet. So increment the no of fleets
            # and change fleet time to the time of the current car. As
            # there is no other car between the fleet and the current car.
            # If a car has lower reach time than the current fleet, that
            # car will collied with the fleet and hence no need to increment
            # the no of fleet as fleet time will remain the same.
            # Remember the fleet time is decided by the first car of the fleet.
            if reach_time > fleet_time:
                fleet_time = reach_time
                fleets += 1
                
            
        return fleets