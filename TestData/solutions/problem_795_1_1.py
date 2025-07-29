class Solution:
    def solution_795_1_1(self, a, b):
        self.parent[self.solution_795_1_2(a)] = self.solution_795_1_2(b)
		
    def solution_795_1_2(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.solution_795_1_2(self.parent[a])

        return self.parent[a]
        
    def solution_795_1_3(self, s: str, pairs: List[List[int]]) -> str:
		# 1. Union-Find
        self.parent = list(range(len(s)))
        for a, b in pairs:
            self.solution_795_1_1(a, b)

		# 2. Grouping
        group = defaultdict(lambda: ([], []))  
        for i, ch in enumerate(s):
            parent = self.solution_795_1_2(i)
            group[parent][0].append(i)
            group[parent][1].append(ch)

		# 3. Sorting
        res = [''] * len(s)
        for ids, chars in group.values():
            ids.sort()
            chars.sort()
            for ch, i in zip(chars, ids):
                res[i] = ch
                
        return ''.join(res)