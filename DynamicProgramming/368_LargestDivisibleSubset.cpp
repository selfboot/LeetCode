/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-03 09:06:44
 */


class Solution {
public:
    /*
    Dynamic Programming!
    For an increasingly sorted array of integers a[0 .. n-1]
    dp[n]: the length of the largest divisible subset whose largest number is a[n]
    Then dp[n+1] = max{ 1 + T[i] if a[n+1] % a[i] == 0 else 1 } for i in [0:n+1].
    For the final result we will need to maintain a backtrace array for the answer.

    For more details, look at:
    https://leetcode.com/discuss/110914/c-solution-with-explanations
    */
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        int length = nums.size();
        if(length==0){
            return {};
        }
        sort(nums.begin(), nums.end());
        vector<int> pre_num(length, 0);
        vector<int> dp(length, 1);

        int max_len = 1;
        int max_pos = 0;
        for(int i=1; i<length; i++){
            for(int j=0; j<i; j++){
                if(nums[i] % nums[j] == 0 && dp[i] < dp[j]+1){
                    dp[i] = dp[j]+1;
                    pre_num[i] = j;
                    if(dp[i] > max_len){
                        max_len = dp[i];
                        max_pos = i;
                    }
                }
            }
        }

        vector<int> ans;
        for(int i=0; i<max_len; i++){
            ans.push_back(nums[max_pos]);
            max_pos = pre_num[max_pos];
        }

        return ans;
    }
};

/*
[]
[1]
[2,3]
[1,2,4,8]
[54,3,24,18,6,9,12]
[2,3,18,24,72,108,216]
*/
