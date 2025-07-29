class Solution:
    def solution_1577_4(self, messages: List[str], senders: List[str]) -> str:
        d = defaultdict(list)
        
        for m, s in zip(messages, senders):
            d[s].append(m)

        longest = [0, []]
        for s in d:
            l = 0
            for m in d[s]:
                l += len(m.split())
            if l > longest[0]:
                longest[0] = l
                longest[1] = [s]
            elif l == longest[0]:
                longest[1].append(s)
                    
        return max(longest[1])