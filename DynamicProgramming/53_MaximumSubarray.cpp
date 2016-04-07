/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-07 11:08:44
 */


class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int nums_len = nums.size();
        int pre_sum = nums[0];
        int max_sum = nums[0];

        for(int i=1;i<nums_len;i++){
            pre_sum = max(pre_sum+nums[i], nums[i]);
            max_sum = max(max_sum, pre_sum);
        }
        return max_sum;
    }
};

/*
[-1]
[1]
[-9,-2,-3,-5,-3]
[-2,1,-3,4,-1,2,1,-5,4]
*/
