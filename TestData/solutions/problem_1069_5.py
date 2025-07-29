class Solution:
    def solution_1069_5(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        # iterate through the pairs
        # add pairs to d: d[x] = y, d[y] = x
        # check each pair x, y in preferences to see if
        # for friends in preferences[x][:indexy]:
        #    check the condition

        pd = {}
        for x, y in pairs:
            pd[x] = y
            pd[y] = x

        unhappy = 0
        for x in pd.keys():
            y = pd[x]
            indexy = preferences[x].index(y)
            betterFriends = preferences[x][:indexy]

            for u in betterFriends:
                v = pd[u]
                indexv = preferences[u].index(v)

                if x in preferences[u][:indexv]:
                    unhappy += 1
                    break

        return unhappy