class Solution:
    def solution_1416_4(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key = lambda x: (x[0]))
        base = [i for i in range(len(queries))]
        partialRes = {}
        i = beauty = 0
        for query, b in sorted(zip(queries, base), key = lambda x: x[0]):
            while i < len(items) and items[i][0] <= query:
                beauty = max(beauty, items[i][1])
                i += 1
            partialRes[b] = beauty
        return [beauty for b, beauty in sorted(partialRes.items(), key = lambda x:x[0])]