/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-25 18:31:59
 */

class Solution {
public:
    /*
    Search from left to right and maintain a max height of left and right separately,
    which is like a one-side wall of partial container.
    Fix the higher one and flow water from the lower part.
    For example, if current height of left is lower,
    we fill water in the left bin.
    Until left meets right, we filled the whole container.

    Brilliant solution proposed by @mcrystal
    Refer to: https://discuss.leetcode.com/topic/5125/sharing-my-simple-c-code-o-n-time-o-1-space
    */
    int trap(vector<int>& height) {
        int max_left=0, max_right = 0;
        int left = 0, right = height.size()-1;
        int ans = 0;
        while(left <= right){
            if(height[left] <= height[right]){
                if(height[left] >= max_left){
                    max_left = height[left];
                }
                else{
                    ans += max_left - height[left];
                }
                left ++;
            }
            else{
                if(height[right] >= max_right){
                    max_right = height[right];
                }
                else{
                    ans += max_right - height[right];
                }
                right --;
            }
        }
        return ans;
    }
};

/*
[]
[3,0,0,3]
[1,1,1,2,2,1,1]
[0,1,0,2,1,0,1,3,2,1,2,1]
*/
