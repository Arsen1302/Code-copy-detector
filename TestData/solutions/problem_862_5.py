class Solution:
    def solution_862_5(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        friends_already_visited=set()
        friends_at_last_level=set([id])
        for l in range(0,level):
            friends_already_visited.update(list(friends_at_last_level))
            newfriends=set()
            for oldfriend in friends_at_last_level:
                newfriends.update(friends[oldfriend])
            friends_at_last_level=newfriends.difference(friends_already_visited)
        video_freq=dict()
        for friend in friends_at_last_level:
            for video in watchedVideos[friend]:
                if video not in video_freq:
                    video_freq[video]=0
                video_freq[video]+=1
        return [video for video,freq in sorted(video_freq.items(), key= lambda item : (item[1], item[0]))]