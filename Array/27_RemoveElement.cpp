/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-06 21:03:01
 */

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int val_start = 0;
        for(auto &n : nums){
            if(n!=val){
                nums[val_start++] = n;
            }
        }
        return val_start;
    }
};

/*
[]
0
[2,2,2,3,3,3,5,5,5]
4
[1,2,3,4,5,1,2,3,4,5]
3
*/
