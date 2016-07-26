/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-26 09:32:27
 */

class Solution {
public:
    /*
    When you can reach position i, find the next longest distance you can reach.

    Once we can reach position i, we can find the next longest distance by iterate all
    the position before position i.

    Of course, you can think it as a BFS problem.
    Where nodes in level i are all the nodes that can be reached in i-1th jump.
    For more explnation, goto:
    https://discuss.leetcode.com/topic/3191/o-n-bfs-solution
    */
    int jump(vector<int>& nums) {
        if(nums.size() == 1)    return 0;
        int step = 1, longest = nums[0];
        int index = 1;
        while(longest < nums.size()-1){
            int max_instance = 0;
            while(index <= longest){
                if(index + nums[index] > max_instance){
                    max_instance = index + nums[index];
                }
                index += 1;
            }
            step += 1;
            longest = max_instance;
        }
        return step;
    }
};

/*
[0]
[2,5,0,3]
[2,3,1,1,4]
[3,1,8,1,1,1,1,1,5]
*/
