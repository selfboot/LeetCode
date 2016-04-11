/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-11 15:02:03
 */

class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        vector<int> ans(2,0);
        int xor_nums = 0;
        for(int &n : nums){
            xor_nums ^= n;
        }
        xor_nums &= -xor_nums;
        for(int &n : nums){
            /*
             * All the numbers can be partitioned into
             * two groups according to their bits at location i.
             * The first group consists of all numbers whose bits at i is 0.
             * The second group consists of all numbers whose bits at i is 1.
             * The two different number a and b is in the two different groups.
             */
            if(n & xor_nums){
                ans[0] ^= n;
            }
            else{
                ans[1] ^= n;
            }
        }
        return ans;
    }
};

/*
[-1,0]
[1, 2, 1, 3, 2, 5]
[-1,-1,-2,-2,-3,-3,-3,-3,4,-5]
*/
