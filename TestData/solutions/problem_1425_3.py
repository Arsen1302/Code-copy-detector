class Solution:
    def solution_1425_3(self, words1: List[str], words2: List[str]) -> int:
        """d = {}
        for xx in words1:
            d[xx] = 1 + d.get(xx, 0)
        count=0
        for i,j in enumerate(d):
            print(d[j])
            if j in words2 and d[j]==1:
                count+=1
        d = {}
        for xx in words2:
            d[xx] = 1 + d.get(xx, 0)
        coun=0
        for i,j in enumerate(d):
            print(d[j])
            if j in words1 and d[j]==1:
                coun+=1
        return min(count,coun)"""
        freq1, freq2 = Counter(words1), Counter(words2)
        return len({w for w, v in freq1.items() if v == 1} &amp; {w for w, v in freq2.items() if v == 1})