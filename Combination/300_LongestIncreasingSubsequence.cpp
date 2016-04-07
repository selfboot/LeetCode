/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-07 11:38:39
 */


class Solution {
public:
    /*
    The key to the solution is: build a ladder for numbers: dp.
    dp[i]: the smallest num of all increasing subsequences with length i+1.
    When a new number x comes, compare it with the number in each level:
        1. If x is larger than all levels, append it, increase the size by 1
        2. If dp[i-1] < x <= dp[i], update dp[i] with x.

    According to:
    https://leetcode.com/discuss/67554/9-lines-c-code-with-o-nlogn-complexity
    */
    int lengthOfLIS(vector<int>& nums) {
        vector<int> dp;
        for(auto &n : nums){
            auto iter = lower_bound(dp.begin(), dp.end(), n);
            if(iter == dp.end()){
                dp.push_back(n);
            }
            else{
                *iter = n;
            }
        }
        return dp.size();
    }
};


/*
[]
[3]
[1,1,1,1]
[10,9,2,5,3,7,101,18]
*/
