from typing import List

class Twitter:

    def __init__(self):
        self.timer = 0
        # list ki jagah set use karenge taaki duplicate followers na hon
        self.mapping_follower = {}
        self.mapping_tweet = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timer += 1
        if userId in self.mapping_tweet:
            self.mapping_tweet[userId].append((self.timer, tweetId))
        else:
            self.mapping_tweet[userId] = [(self.timer, tweetId)]

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = set()  # set use kiya taaki koi duplicate user id na aaye
        if userId in self.mapping_follower:
            ans.update(self.mapping_follower[userId])
        
        ans.add(userId)
        output = []
        
        # Ab hum poori dictionary par loop nahi chalayenge, 
        # sirf un users ke tweets nikalenge jo 'ans' (followed users + khud) mein hain
        for user in ans:
            if user in self.mapping_tweet:
                output.extend(self.mapping_tweet[user])

        # Tweets ko unke timestamp (timer) ke hisab se descending order mein sort karenge
        output.sort(key=lambda x: x[0], reverse=True)
        
        final = []
        for i, j in output:
            final.append(j)
            if len(final) == 10:
                break

        return final

    def follow(self, followerId: int, followeeId: int) -> None:
        # User khud ko follow nahi karega
        if followerId == followeeId:
            return
            
        if followerId in self.mapping_follower:
            self.mapping_follower[followerId].add(followeeId) # set mein add kiya
        else:
            self.mapping_follower[followerId] = {followeeId} # naya set banaya

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.mapping_follower:
            # .discard() use karne se agar followeeId nahi bhi hoga, toh error nahi aayega
            self.mapping_follower[followerId].discard(followeeId)

            if len(self.mapping_follower[followerId]) == 0:
                del self.mapping_follower[followerId]
