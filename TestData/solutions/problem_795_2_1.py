class Solution:
    def solution_795_2_1(self, s: str, pairs: List[List[int]]) -> str:
        # Start of Union Find Data Structure
        p = list(range(len(s)))  # parent
        # each element in the pairs == node
        # used to store each node's parent based on its index
        # eg. pairs = [[0,3],[1,2]], p = [0, 1, 1, 0]
        # element 3 in pairs == p index 3 == 0 (because parent node of 3 is 0)

        def solution_795_2_2(x):
            if x != p[x]:
                p[x] = solution_795_2_2(p[x])
            return p[x]

        def solution_795_2_3(x, y):
            px = solution_795_2_2(x)
            py = solution_795_2_2(y)
            if px != py:
                p[py] = px
                
        # End of Union Find Data Structure

        # Grouping
        for x, y in pairs:
            solution_795_2_3(x, y)

        dic = defaultdict(list)
        for idx, el in enumerate(p):
            dic[solution_795_2_2(el)].append(idx)
        
        # eg. pairs = [[0,3],[1,2]], dic = {0: [0, 3], 1: [1, 2]}

        # Sorting
        res = list(s)
        for key in dic.keys():
            idx_list = dic[key]
            char_list = [s[i] for i in idx_list]
            char_list.sort()

            # eg. idx_list = [0, 3], char_list = [b, d]
            # for loop below, idx = [0, b], char = [3, d]
            for idx, char in zip(idx_list, char_list):
                res[idx] = char

        return "".join(res)