class Solution:
    def solution_1005_3(self, path: str) -> bool:
        #Store the directions(key) with their corresponding actions(values)
        directions = {'N': [0,1], 'E':[1,0], 'W':[-1,0], 'S':[0,-1]}
        
        #Keep the track of visited points
        visited = set()
        
        #Add the initial point from where you're starting
        visited.add((0,0))
        
        #Current trackers of x and y coordinates
        curr_x,curr_y = 0,0
        
        #Loop through all the path
        for i in path:
            curr_x += directions[i][0]
            curr_y += directions[i][1]
            
            #If visited for first time, add them to visited
            if (curr_x,curr_y) not in visited:
                visited.add((curr_x,curr_y))
            else:
                return True #Else return True
            
        return False #Return True if there is no re-visiting