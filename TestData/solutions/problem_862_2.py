class Solution:
    def solution_862_2(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        friends = [set(lst) for lst in friends]
        row = friends[id]
        previous_friends = {id}
        for _ in range(1, level):
            previous_friends.update(row)
            new_row = set()
            for friend in row:
                new_row.update(friends[friend])
            row = new_row - previous_friends
        videos = defaultdict(int)
        for friend in row:
            for video in watchedVideos[friend]:
                videos[video] += 1
        return [v for _, v in sorted((freq, v) for v, freq in videos.items())]