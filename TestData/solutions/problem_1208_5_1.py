class Solution:
    def solution_1208_5_1(self, cars: List[List[int]]) -> List[float]:
        times = [float(-1) for _ in range(len(cars))]
        for i in range(1, len(cars)):
            if cars[i-1][1] > cars[i][1]:
                times[i-1] = self.solution_1208_5_2(cars, i-1, i)
        for i in range(len(cars)-3, -1, -1):
            if times[i+1] == - 1.0: continue
			# if car[i+1] collided before car[i], then we have to adjust times[i]
            if times[i] > times[i+1]:
                times[i] = self.solution_1208_5_3(cars, times, i)
                cars[i+1][1] = cars[i+2][1]
			# if car[i+1] collided and speed became slower than cars[i], then we also have to adjust times[i]
            elif cars[i][1] <= cars[i+1][1] and times[i+1] > 0.0:
                if cars[i][1] > cars[i+2][1]:
                    times[i] = self.solution_1208_5_2(cars, i, i+2)
        return times
        
    def solution_1208_5_2(self, cars, i, j): 
        return (cars[j][0]-cars[i][0])/(cars[i][1] - cars[j][1])
    def solution_1208_5_3(self, cars, times, i):
        return times[i+1] + (times[i]-times[i+1])*(cars[i][1] - cars[i+1][1])/(cars[i][1] - cars[i+2][1])