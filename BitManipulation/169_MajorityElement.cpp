/*
* @Author: xuelangZF
* @Date:   2016-03-06 17:30:53
* @Last Modified by:   xuelangZF
* @Last Modified time: 2016-03-06 17:30:53
*/

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 0, num = 0, size = nums.size();
        for(int i=0; i<size; i++){
            if (count == 0){
                num = nums[i];
            }
            if (num == nums[i]){
                count += 1;
            }
            else{
                count -= 1;
            }
        }
        return num;
    }
};
