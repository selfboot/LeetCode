/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-27 17:09:34
 */

class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0;
        int right = nums.size()-1;

        /*
        Make sure right is always in the right rotated part.
        Left can be either in the left part or the minimum part.
        So, when left and right is the same finally, we find the minimum.
        */
        while(left<right){
            // When there is no rotate, just return self.nums[start]
            if(nums[left]<nums[right])  return nums[left];
            int mid = left + (right-left) / 2;
            // mid is in the left part, so move the left point to mid+1.
            // finally left will reach to the minimum element.
            if(nums[left] <= nums[mid]){
                left = mid+1;
            }
            else{
                right = mid;
            }
        }
        return nums[left];
    }
};

/*
[1]
[1,2]
[3,4,2]
[7,8,9,0,2,4,5]
*/
