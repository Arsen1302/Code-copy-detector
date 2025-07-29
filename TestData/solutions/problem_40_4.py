class Solution:
    def solution_40_4(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # bfs
        wordList = set(wordList)
        if endWord not in wordList: return 0
        l = len(beginWord)

        begin_queue, end_queue = deque([beginWord]), deque([endWord])
        level = 0
        begin_used, end_used = set(), set()

        while begin_queue and end_queue:
            level += 1
            for _ in range(len(begin_queue)): # level order
                begin_word = begin_queue.popleft()
                begin_used.add(begin_word)
                for i in range(l):
                    for c in string.ascii_lowercase[:26]:
                        w = begin_word[:i] + c + begin_word[i+1:]
                        if w in end_queue: return level * 2
                        if w in wordList and w not in begin_used:
                            begin_queue.append(w)
            for _ in range(len(end_queue)):
                end_word = end_queue.popleft()
                end_used.add(end_word)
                for i in range(l):
                    for c in string.ascii_lowercase[:26]:
                        w = end_word[:i] + c + end_word[i+1:]
                        if w in begin_queue: return level * 2 + 1
                        if w in wordList and w not in end_used:
                            end_queue.append(w)
                            
        return 0