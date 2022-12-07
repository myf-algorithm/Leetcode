class Twitter:
    class Node:
        def __init__(self):
            self.followee = set()
            self.tweet = list()

    def __init__(self):
        self.time = 0
        self.recentMax = 10
        self.tweetTime = dict()
        self.user = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user:
            self.user[userId] = Twitter.Node()
        self.user[userId].tweet.append(tweetId)
        self.time += 1
        self.tweetTime[tweetId] = self.time

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.user:
            return list()
        ans = self.user[userId].tweet[-10:][::-1]
        for followeeId in self.user[userId].followee:
            if followeeId in self.user:
                opt = self.user[followeeId].tweet[-10:][::-1]
                i, j, combined = 0, 0, list()
                while i < len(ans) and j < len(opt):
                    if self.tweetTime[ans[i]] > self.tweetTime[opt[j]]:
                        combined.append(ans[i])
                        i += 1
                    else:
                        combined.append(opt[j])
                        j += 1
                combined.extend(ans[i:])
                combined.extend(opt[j:])
                ans = combined[:10]
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followerId not in self.user:
                self.user[followerId] = Twitter.Node()
            self.user[followerId].followee.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followerId in self.user:
                self.user[followerId].followee.discard(followeeId)
