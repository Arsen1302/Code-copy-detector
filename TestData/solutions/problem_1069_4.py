class Solution:
    def solution_1069_4(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        likemore = {}
        for a,b in pairs:
            likemore[a] = set(preferences[a][:preferences[a].index(b)])
            likemore[b] = set(preferences[b][:preferences[b].index(a)])
        unhappy = set()
        for i in range(n):
            for j in range(i):
                if(i in likemore[j] and j in likemore[i]):
                    unhappy.add(i)
                    unhappy.add(j)
        return len(unhappy)