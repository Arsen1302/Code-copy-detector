class Solution:
    def solution_1637_1(self, nums: List[int]) -> bool:
        idxs = defaultdict(list)
        n = len(nums)
        
        #Find all doubles
        for idx in range(1, n):
            if nums[idx] == nums[idx - 1]:
                idxs[idx - 1].append(idx + 1)
                
        #Find all triples
        for idx in range(2, n):
            if nums[idx] == nums[idx - 1] == nums[idx - 2]:
                idxs[idx - 2].append(idx + 1)
                
        #Find all triple increments
        for idx in range(2, n):
            if nums[idx] == nums[idx - 1] + 1 == nums[idx - 2] + 2:
                idxs[idx - 2].append(idx + 1)
        
        #DFS 
        seen = set()
        stack = [0]

        while stack:
            node = stack.pop()

            if node not in seen:
                if node == n:
                    return True
                seen.add(node)

            for adj in idxs[node]:
                if adj not in seen:
                    stack.append(adj)
        
        return False