class Solution:
    def solution_369_3_1(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        memo = dict()

        def solution_369_3_2(remain):
            if tuple(remain) in memo:
                return memo[tuple(remain)]

            ans = math.inf
            for i in range(len(special)):
                if not any([special[i][j] > remain[j] for j in range(len(remain))]):
                    for j in range(len(price)):
                        remain[j] -= special[i][j]

                    ans = min(ans, solution_369_3_2(remain) + special[i][-1])
                    
                    for j in range(len(price)):
                        remain[j] += special[i][j]
            
            memo[tuple(remain)] = min(ans, sum([num * price for num, price in zip(remain, price)]))
            return memo[tuple(remain)]
        
        return solution_369_3_2(needs)