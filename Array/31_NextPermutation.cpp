/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-07 21:09:56
 */


class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        if(nums.empty())    return;
        int i;
        for(i=nums.size()-1; i>=1; i--){
            if(nums[i] > nums[i-1]) break;
        }
        reverse(nums.begin()+i, nums.end());
        if(i==0)    return;
        auto iter = upper_bound(nums.begin()+i, nums.end(), nums[i-1]);
        swap(nums[i-1], *iter);
    }
};

/*
[]
[1]
[1,2,3]
[3,2,1]
[1,1,2,2,4,5,5]
*/
