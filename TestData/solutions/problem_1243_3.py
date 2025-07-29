class Solution:
        def solution_1243_3(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
                #create a empty list k 
                k = []
                #create a variable and initialise it to 0 
                count = 0 
                #iterate over the elements in the queries
                for i in queries:
                        #in each sublist 1st element is x co-ordinate
                        x1 = i[0]
                        #in each sublist 2nd element is y co-ordinate
                        y1 = i[1]
                        #in each sublist 3rd element is radius
                        r = i[2]
                        #iterate ovet the lists in points
                        for j in points:
                                #in each sublist 1st element is x co-ordinate
                                x2 = j[0]
                                #in each sublist 2nd element is y co-ordinate
                                y2 = j[1]
                                #if the distance between those two co-ordinates is less than or equal to radius 
                                if (((x2 - x1)**2 + (y2 - y1)**2)**0.5) <= r :
                                        #then the point lies inside the cirle or on the circle
                                        #then count how many points are inside the circle or on the circle by incrementing count variable
                                        count = count + 1
                        
                        #after finishing one co-ordinate in points then add the count value in list k                
                        k.append(count)
                        #then rearrange the value of count to 0 before starting next circle 
                        count = 0 
                #after finishing all circles return the list k 
                return k