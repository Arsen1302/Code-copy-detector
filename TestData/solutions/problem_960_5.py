class Solution:
def solution_960_5(self, paths: List[List[str]]) -> str:
    city_from, city_to = [], []
	
    for i in range(len(paths)):
        city_from.append(paths[i][0])
        city_to.append(paths[i][1])
        
    for city in city_to:
        if city not in city_from:
            return city