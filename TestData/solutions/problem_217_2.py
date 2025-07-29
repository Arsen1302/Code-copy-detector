class Solution:
    def solution_217_2(self, people: List[List[int]]) -> List[List[int]]:
        from sortedcontainers import SortedList
        n = len(people)
        people.sort()
        ans = [None] * n
        ans[people[0][1]] = people[0]
        sl = SortedList(range(n))
        toRemove = [people[0][1]]
        for i in range(1, n):
            if people[i][0] != people[i - 1][0]:
                for index in toRemove:
                    sl.remove(index)
                toRemove = []
            ans[sl[people[i][1]]] = people[i]
            toRemove.append(sl[people[i][1]])
        return ans