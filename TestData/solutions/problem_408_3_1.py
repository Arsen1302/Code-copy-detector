class Solution:
     
    @staticmethod
    def solution_408_3_1(c1, c2):
	    # remove intersection of c1 and c2 from c2 and encode the c1 to string
        remove_keys = []
        result = ""
        for k in c1.keys():
            if k in c2:
                c1[k] -= c2[k]
                if c1[k] <= 0:
                    remove_keys.append(k)
            if c1[k] > 0:
                result += k + str(c1[k])
        
        for key in remove_keys:
            c1.pop(key, None)
        return c1, result
                
    def solution_408_3_2(self, stickers: List[str], target: str) -> int:
	    # count all letters in target
        target_count = Counter(target)
        stickers_counter = []
        
        s1 = set(target_count.keys())
        s2 = set()
        
		# count all letters which are exist in target for every sticker
        for i in range(len(stickers)):
            sticker = stickers[i]
            sticker_counter = defaultdict(int)
            for letter in sticker:
                if letter in target_count:
                    sticker_counter[letter] += 1
            stickers_counter.append(sticker_counter)
            s2.update(sticker_counter.keys())
        
        if s2 != s1:
            return -1
        
        total_letters = sum(target_count.values())
        counter = 0
        
        q = deque([target_count])
        visited = set()
        
		# BFS loop to find the shortest path to get empty target dict
        while q:
            q_size = len(q)
            for _ in range(q_size):
                target_count = q.popleft()
                for sticker in stickers_counter:
                    tmp, encoded = self.solution_408_3_1(target_count.copy(), sticker)
                    if sum(tmp.values()) == 0:
                        return counter+1
                    if encoded not in visited:
                        q.append(tmp)
                        visited.add(encoded)
            counter += 1
        return -1