class Solution(object):
    def solution_906_5(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        counts = collections.defaultdict(list)
        for vote in zip(*votes):
            cntr = collections.Counter(vote)
            for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                counts[ch] += [-1*cntr[ch]]
        return "".join(sorted(votes[0],key=lambda x :counts[x]+[x]))