import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.timer = 0
        # Maps userId -> set of followeeIds
        self.mapping_follower = defaultdict(set)
        # Maps userId -> list of tuples (timer, tweetId)
        self.mapping_tweet = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timer += 1
        # Append the tweet with a timestamp. Keep only the 10 most recent 
        # tweets per user to bound memory consumption if desired.
        self.mapping_tweet[userId].append((self.timer, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        
        # A user automatically sees their own tweets
        users_to_fetch = self.mapping_follower[userId] | {userId}
        
        for u_id in users_to_fetch:
            tweets = self.mapping_tweet[u_id]
            # Since tweets are appended chronologically, the most recent ones are at the end
            # Fetch up to the last 10 tweets for each target user
            for t_time, t_id in tweets[-10:]:
                heapq.heappush(min_heap, (t_time, t_id))
                if len(min_heap) > 10:
                    heapq.heappop(min_heap)
                    
        # The heap contains the 10 most recent tweets, but the smallest timestamp is at the root.
        # Pop them out and reverse to get most-recent-first order.
        ans = []
        while min_heap:
            ans.append(heapq.heappop(min_heap)[1])
            
        return ans[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.mapping_follower[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.mapping_follower[followerId]:
            self.mapping_follower[followerId].remove(followeeId)
