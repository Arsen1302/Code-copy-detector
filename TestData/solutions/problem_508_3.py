class Solution:
    def solution_508_3(self, words: List[str]) -> int:
        trie = (d := lambda: defaultdict(d))()  # multi-level collections.defaultdict
        for word in words:
            curr = trie
            for i in range(len(word)):
                curr = curr[word[~i]]
        return (dfs := lambda node, curr: sum(dfs(adj, curr+1) for adj in node.values()) if node else curr)(trie, 1)