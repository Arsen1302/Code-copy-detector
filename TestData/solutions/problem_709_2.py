class Solution:
    def solution_709_2(self, costs: List[List[int]]) -> int:
        '''
        Example:
        [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
        
        Answer Choices (what to choose for min cost):
        City A - 259, 184, 577 
        City B - 54, 118, 667
        Answer Total Score: 1859
        
        Calculate scores for each pair and determine which cities to pick.
        Higher score = higher priority to pick lower cost city
        
        Score = abs(cityA - cityB)
        
        722 - [840, 118] - City B
        511 - [259, 770] - City A
        394 - [448, 54] - City B
        259 - [926, 667] - City B
        108 - [577,459] - City A
        45 - [184, 139] - City A
        '''
        people = len(costs) / 2
        a,b = people,people

        scores = [[abs(a-b),(a,b)] for a,b in costs] # calc the score, store the pair
        scores.sort(reverse=True)
        
        totalScore = 0
        # Scores - [[Calculated Score, (CityA-Cost, CityB-Cost)], ... ] This is what the scores array looks like
        for x in scores:
            choice = x[1]
            if choice[0] <= choice[1] and a > 0 or b == 0: # b == 0 means we reached n choices for city B already
                a -= 1
                totalScore += choice[0]
            elif choice[0] > choice[1] and b > 0 or a == 0:
                b -= 1
                totalScore += choice[1]
        return totalScore