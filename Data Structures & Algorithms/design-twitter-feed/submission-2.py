class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.idx=0        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([tweetId, self.idx])
        self.idx+=1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        heap=[]
        self.following[userId].add(userId)
        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                i=len(self.tweets[followeeId])-1
                tweetId,count = self.tweets[followeeId][i]
                heapq.heappush(heap,[-count,tweetId,followeeId,i])
        res=[]

        while heap and len(res)<10:
            count,tweetId,followeeId,i=heapq.heappop(heap)
            res.append(tweetId)

            if i>0:
                i-=1
                tweetId,count=self.tweets[followeeId][i]
                heapq.heappush(heap,[-count,tweetId,followeeId,i])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

        
'''
tc: 
postTweet() → O(1)
follow() → O(1)
unfollow() → O(1)
getNewsFeed() → O(F log F)   where F = number of users being followed (including yourself).

sc:
getNewsFeed() → O(F) heap space

following = {}
tweets = {}
idx = 0


Input:
["Twitter", "postTweet", [1, 10], "postTweet", [2, 20], "getNewsFeed", [1], "getNewsFeed", [2], "follow", [1, 2], "getNewsFeed", [1], "getNewsFeed", [2], "unfollow", [1, 2], "getNewsFeed", [1]]


postTweet(1,10)
tweets = {1: (10,0)}
idx=1

postTweet(2, 20)
tweets = {1: (10,0), 2: (20,1)}
idx=2

getNewsFeed(1) - 10

getNewsFeed(2) - 20

follow(1,2)

following = {1:{2}}

getNewsFeed(1) - 20 10

getNewsFeed(1) - 20

unfollow(1,2) 
following={}

getNewsFeed(1) - 10










'''