/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-28 10:57:41
 */

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        // Every time put the non-zero number to the right position.
        int non_zero = 0, index = 0;
        for(; index<nums.size(); index++){
            if(nums[index] != 0){
                if(index != non_zero){
                    swap(nums[index], nums[non_zero]);
                }
                non_zero += 1;
            }
        }
    }
};

/*
[]
[1]
[0]
[0,0,0]
[0,1,0,3,12]
[7,6,5,4,0,4,0,5,6,0,7,0,0]
*/
