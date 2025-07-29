class Solution:
    def solution_1707_3(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:

        # make a dict to save the viwer count and the highest view count
        counter = collections.defaultdict(lambda: [0, "", -1])

        # go through the content creators
        for creator, idd, view in zip(creators, ids, views):

            # get the list with informations
            infos = counter[creator] 

            # increase the view
            infos[0] += view

            # check if the video is the most viewed
            if view > infos[2] or (view == infos[2] and infos[1] > idd):
                infos[2] = view
                infos[1] = idd
        
        # go through the creators and keep the highes
        result = []
        max_count = -1
        for creator, infos in counter.items():

            # check if we are higher or equal to current count
            if max_count <= infos[0]:

                # check if we are higher than current max
                if max_count < infos[0]:
                    # clear the list
                    result.clear()
                    # update the max count
                    max_count = infos[0]
                
                # append our current content creator
                result.append([creator, infos[1]])
        return result