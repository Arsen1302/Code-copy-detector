class Solution:
    def solution_838_4(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}
        for i in range(len(groupSizes)): # creating a dictionary to group all persons that have the same groupSize
            if groupSizes[i] not in d:
                d[groupSizes[i]] = []
                d[groupSizes[i]].append(i)
            else:
                d[groupSizes[i]].append(i)
        res = []
        k = 0 # index of the list we return
        for i, ele in enumerate(d): # we iterate through the dictionary and every list
            count = 0
            res.append([])
            for j in range(len(d[ele])):
                res[k].append(d[ele][j])
                count += 1    # we count how many persons we add -> if there are more persons than the number of groupSize we append another empty list
                if count == ele:
                    if j < len(d[ele])-1:
                        res.append([])
                        k += 1
                    count = 0
            k += 1
        return res