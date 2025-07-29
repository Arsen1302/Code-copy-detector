class Solution:
    def solution_1707_4(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        """
        summary : each creator will get to be a key in a  dictionary that contains
        the 1st item the sum of all the views so far
        the 2nd the id(in case if the value of max seen is the same the smallest one lexicographically)
        the 3rd item the maxviews so far

        when we have all this data we look for the biggest sum and append the name of the creator and the id
        to the ans list
        """
        data = {}
        for creator, id , view in zip(creators, ids, views):
            if creator in data:
                data[creator][0] += view
                if  view>data[creator][2]:
                    data[creator][2] = view
                    data[creator][1] = id
                    continue
                if  view==data[creator][2] and id< data[creator][1]:
                    data[creator][1] = id
                    continue
            else:
                data[creator] = [view,id,view]
        maxView = 0
        ans = []
        for k,v in data.items():
            if v[0]>maxView:
                ans =[]
                maxView =v[0]
            if v[0]==maxView:
                ans.append([k,v[1]])
        return ans