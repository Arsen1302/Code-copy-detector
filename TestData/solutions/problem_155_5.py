class Solution:
    def solution_155_5(self, words: List[str]) -> int:
        n = len(words)
        best = 0
        trie = {}

        # Build a trie
		# O(N * U * logU) where U is the number of unique letters (at most 26), simplified to O(N)
        for word in words:
            node = trie
            letters = sorted(set(word))

            for char in letters:
                if char not in node:
                    node[char] = {}
                node = node[char]

            # The "None" node will store the length of the word
            node[None] = max(node.get(None, 0), len(word))

        # Loop through each word
		# O(N)
        for word in words:
            letters = set(word)
            word_len = len(word)

            # With BFS find the longest word inside the trie that does not have any common letters with current word
			# O(2^26 - 1) => O(1)
            queue = collections.deque([trie])

            while queue:
                node = queue.popleft()

                if None in node:
                    best = max(best, node[None] * word_len)

                # Explore the neighbors
                for char in node.keys():
                    if char is not None and char not in letters:
                        queue.append(node[char])

        return best