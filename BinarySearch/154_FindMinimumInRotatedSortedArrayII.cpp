/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-27 18:29:44
 */

class Solution {
public:
    /*
    Make sure right is always in the right rotated part.
    Left can be either in the left part or the minimum part.
    So, when left and right is the same finally, we find the minimum.
    */
    int findMin(vector<int>& nums) {
        int left=0;
        int right=nums.size()-1;
        while(left<right){
            // When there is no rotate, just return self.nums[start]
            if(nums[left] < nums[right])   return nums[left];
            int mid = left + (right-left)/2;
            if(nums[left] < nums[mid]){
                left = mid+1;
            }
            else if(nums[left] > nums[mid]){
                right = mid;
            }
            // Can't make sure whether left is in the left part or not.
            // Just move to right for 1 step.
            else{
                left += 1;
            }
        }
        return nums[left];
    }
};

/*
[1]
[7,8,9,9,9,10,2,2,2,3,4,4,5]
*/
