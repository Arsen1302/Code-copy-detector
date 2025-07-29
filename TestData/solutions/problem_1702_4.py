class Solution:
    def solution_1702_4(self, words):
        d = defaultdict(list)
        for w in words:
            f = [ord(w[i+1])-ord(w[i]) for i in range(len(w)-1)]
            d[tuple(f)].append(w)
        for x in d:
            if len(d[x])==1:
                return d[x][0]