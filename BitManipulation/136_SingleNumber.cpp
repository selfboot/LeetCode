/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-11 23:02:26
 */

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int xor_n = 0;
        for(const auto &n: nums){
            xor_n ^= n;
        }
        return xor_n;
    }
};
