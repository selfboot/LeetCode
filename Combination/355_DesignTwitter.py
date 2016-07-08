#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-07-08 13:57:50


class Twitter(object):
    """
    Accordting to:
    https://discuss.leetcode.com/topic/47838/python-solution
    """
    def __init__(self):
        self.timer = itertools.count(step=-1)
        self.tweets = collections.defaultdict(collections.deque)
        self.followees = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        """Compose a new tweet.
        """
        self.tweets[userId].appendleft((next(self.timer), tweetId))

    def getNewsFeed(self, userId):
        """Retrieve the 10 most recent tweet ids in the user's news feed.

        Each item in the news feed must be posted by users who the user
        followed or by the user herself.
        Tweets must be ordered from most recent to least recent.
        """
        tweets = heapq.merge(*(self.tweets[u] for u in
                              (self.followees[userId] | {userId})))
        return [t for _, t in itertools.islice(tweets, 10)]

    def follow(self, followerId, followeeId):
        """Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followees[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

"""
["Twitter","postTweet","postTweet","getNewsFeed","postTweet","getNewsFeed"]
[[],[1,5],[1,3],[3,5],[1,6],[3,5,6]]
["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]
[[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]
"""
