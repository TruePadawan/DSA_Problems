import time
from typing import Dict, List, Set, TypedDict

"""
The Twitter object manages users and their posts
The relevant data for each user is:
    userId: <int>
    tweets - [{
        tweetId: <string>,
        postedOn: <timestamp>
    }]
    followers - [followerId,...]
    users they're following - [followeeId,...]
Each user should be stored in a dict with the key being their userId and value being the rest of the data
userId: {
    tweets, [],
    followers: [],
    following: []
}
"""


# Types for sanity
class Tweet(TypedDict):
    tweetId: str
    postedOn: float


class UserData(TypedDict):
    tweets: List[Tweet]
    followers: Set[int]
    following: Set[int]


class Twitter:
    def __init__(self):
        self.users: Dict[str, UserData] = {}

    def createUser(self, userId: int) -> None:
        if self.users.get(userId) is None:
            self.users[userId] = {"tweets": [], "followers": set(), "following": set()}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.createUser(userId)
        self.users[userId]["tweets"].append(
            {"tweetId": tweetId, "postedOn": time.time()}
        )

    def getNewsFeed(self, userId: int) -> List[int]:
        # Create the user if they don't exist
        self.createUser(userId)
        
        # Join the users posts and the posts of the users they're following
        # No way this is going to pass all the testcases
        tweets = self.users[userId]["tweets"].copy()
        for followeeId in self.users[userId]["following"]:
            followeeTweets = self.users[followeeId]["tweets"]
            tweets.extend(followeeTweets)
        tweets.sort(key=lambda tweet: tweet["postedOn"], reverse=True)
        raw_recent_ten = map(lambda tweet: tweet["tweetId"], tweets[:10])
        parsed_feed = list(raw_recent_ten)
        return parsed_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        # A user cannot follow themself
        if followerId == followeeId:
            return
        
        # Create either/both of the users if they don't exist (Why?)
        self.createUser(followeeId)
        self.createUser(followerId)
        
        self.users[followerId]["following"].add(followeeId)
        self.users[followeeId]["followers"].add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # A user cannot unfollow themself
        if followerId == followeeId:
            return
        
        # Create either/both of the users if they don't exist (Why?)
        self.createUser(followeeId)
        self.createUser(followerId)
        
        self.users[followerId]["following"].discard(followeeId)
        self.users[followeeId]["followers"].discard(followerId)
