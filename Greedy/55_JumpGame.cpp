/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-06-27 13:06:01
 */

class Solution {
public:
    bool canJump(vector<int>& nums) {
        /*
        The main idea is to see if current element can be
        reached by previous max jump.
        If not, return false. If true, renew the max jump.
        */
        int length = nums.size();
        int max_distance = nums[0];

        for(int i=0; i<length; i++){
            if(max_distance >= length-1){
                return true;
            }
            if(max_distance >= i){
                max_distance = max(max_distance, i+nums[i]);
            }
            else{
                return false;
            }
        }
        return true;
    }
};

/*
[0]
[2,3,1,1,4]
[3,2,1,0,4]
[1,3,5,0,0,0,0,0]
*/
