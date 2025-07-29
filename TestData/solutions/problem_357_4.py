class Solution:
    def solution_357_4(self, paths: List[str]) -> List[List[str]]:
        h = defaultdict(list)
        for path in paths:
            files = path.split(' ')
            dr = files[0]
            for file in files[1:]:
                i = file.index('(')
                content = file[i:][1:-1]
                filename = file[:i]
                h[content].append(dr + '/' + filename)
        res = []
        for c in h:
            if len(h[c]) > 1:
                res.append(h[c])
        return res