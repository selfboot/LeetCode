/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-20 10:38:44
 */

class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> ans;
        sort(nums.begin(), nums.end());
        helper(nums, 0, ans);
        return ans;
    }

    void helper(vector<int> num, int begin, vector<vector<int>> &ans){
        // num is passed by value
        if(begin==num.size()-1){
            ans.push_back(num);
            return;
        }
        for(int i=begin;i<num.size();i++){
            if(i!=begin && num[i]==num[begin])  continue;
            swap(num[i], num[begin]);
            helper(num, begin+1, ans);
            // No Backtracking here!!!
        }
    }
};


class Solution_2{
public:
    /*
     * 1. sort nums in ascending order, add it to res;
     * 2. generate the next permutation of nums, and add it to res;
     * 3. repeat 2 until the next permutation of nums returns to the sorted condition in 1.
     */
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> ans;
        sort(nums.begin(), nums.end());
        ans.push_back(nums);
        while(nextPermutation(nums)){
            ans.push_back(nums);
        }
        return ans;
    }

    bool nextPermutation(vector<int>& nums) {
        if(nums.empty())    return false;
        int i;
        for(i=nums.size()-1; i>=1; i--){
            if(nums[i] > nums[i-1]) break;
        }
        reverse(nums.begin()+i, nums.end());
        if(i==0)    return false;
        auto iter = upper_bound(nums.begin()+i, nums.end(), nums[i-1]);
        swap(nums[i-1], *iter);
        return true;
    }
};

/*
[]
[1]
[1,2,3]
[2,2,3,3]
*/
