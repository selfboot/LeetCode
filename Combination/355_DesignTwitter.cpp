/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-08 15:10:06
 */

class Twitter {
    struct Tweet
    {
        int time;
        int id;
        Tweet(int time, int id) : time(time), id(id) {}
    };

    struct compare{
        bool operator()(const Tweet x, const Tweet y) {
            return x.time < y.time;
        }
    };

    int time;
    unordered_map<int, vector<Tweet>> tweets;
    unordered_map<int, unordered_set<int>> followees;

public:
    /** Initialize your data structure here. */
    Twitter(): time(0) {
    }

    /** Compose a new tweet. */
    void postTweet(int userId, int tweetId) {
        tweets[userId].push_back(Tweet(time++, tweetId));
    }

    /** Retrieve the 10 most recent tweet ids in the user's news feed.
    Each item in the news feed must be posted by users who the user
    followed or by the user herself.
    Tweets must be ordered from most recent to least recent. */
    vector<int> getNewsFeed(int userId) {
        priority_queue<Tweet, vector<Tweet>, compare> allnews;
        for(auto u: followees[userId]){
            for(auto &t: tweets[u]){
                allnews.push(t);
            }
        }
        for(auto &t: tweets[userId]){
            allnews.push(t);
        }
        vector<int> ans;
        for(int i=0; i<10 && !allnews.empty(); i++){
            ans.push_back(allnews.top().id);
            allnews.pop();
        }
        return ans;
    }

    /** Follower follows a followee. If the operation is invalid,
    it should be a no-op. */
    void follow(int followerId, int followeeId) {
        if(followerId != followeeId){
            followees[followerId].insert(followeeId);
        }
    }

    /** Follower unfollows a followee. If the operation is invalid,
    it should be a no-op. */
    void unfollow(int followerId, int followeeId) {
        followees[followerId].erase(followeeId);
    }
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * vector<int> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */

/*
["Twitter","postTweet","postTweet","getNewsFeed","postTweet","getNewsFeed"]
[[],[1,5],[1,3],[3,5],[1,6],[3,5,6]]
["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]
[[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]
*/
