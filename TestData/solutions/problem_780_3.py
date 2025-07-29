class Solution:
    def solution_780_3(self, queries: List[str], words: List[str]) -> List[int]:
        q = []
        for query in queries:
            query = sorted(query)
            temp  = query.count(query[0])
            q.append(temp)
        w = []
        for word in words:
            word = sorted(word)
            temp = word.count(word[0])
            w.append(temp)
        ans = []
        w.sort()
        for i in q:
            temp = 0
            for j in range(len(w)):
                if w[j]>i:
                    temp+=len(w)-j
                    break
            ans.append(temp)
        return ans