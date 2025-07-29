class Solution:
    def solution_508_4(self, words: List[str]) -> int:
        words = list(set(words))
        trie = (d := lambda: defaultdict(d))()
        nodes = [reduce(dict.__getitem__, word[::-1], trie) for word in words]  # equivalent to trie[word[-1]][word[-2]]...
        return sum((len(word)+1) for word, node in zip(words, nodes) if len(node) == 0)