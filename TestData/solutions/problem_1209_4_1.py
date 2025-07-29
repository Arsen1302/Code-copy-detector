class Solution:
    def solution_1209_4_1(self, x: int, y: int, points: List[List[int]]) -> int:
        valid_pair = []                                        #Initializing an empty array
        distance_holder = (9999,9999)                          #creating default values for distance holder    

        
        def solution_1209_4_2(x,y,x_point,y_point):        #helper function to calculate manhattan distance
            return abs(x-x_point) + abs(y-y_point)
            
        for idx,pair in enumerate(points):                     #iterate through the points and keep index
            x_point,y_point = pair                             #unpack pairs into x/y points
            
            if x==x_point or y==y_point:                       #checking if x or y equal points
                distance = solution_1209_4_2(x,y,x_point,y_point)  #get manhattan distance
                if distance <= distance_holder[1]:             #check if distance is less than what's currently in holder
                    if distance == distance_holder[1]:         #check if distances are equal to each other
                        distance_holder = (min(distance_holder[0],idx),distance)    #if distances are equal only use minimum index
                    else:
                        distance_holder = (idx,distance)       #update distance holder
                valid_pair.append(distance_holder)             #this was a remnant of brainstorming ways to solve problem , would need to refactor logic to remove this    
            
        if not valid_pair:                                     #checks if any elements are in valid pair
            return -1
        else:
            return distance_holder[0]                #returns index
			```