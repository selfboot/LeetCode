/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-29 10:53:41
 */

class Solution {
public:
    /*
    Sort needed.
    Sort the array(small to big), and cut into two parts:
        For even size, left half size==right half size,
        For odd size,  left half size==right half size+1.
        (smaller part there may be one more number.)

    Then put the smaller half of the numbers on the even indexes,
    and the larger half on the odd indexes.
    Here iterate from the back of two halves,
    so that the duplicates between two parts can be split apart.

    Clear solutionm, explanation and proof can be found here:
    https://leetcode.com/discuss/76965/3-lines-python-with-explanation-proof
    */
    void wiggleSort(vector<int>& nums) {
        vector<int> sorted(nums);
        sort(sorted.begin(), sorted.end());
        int left = (nums.size()+1) / 2, right = nums.size();
        for(int i=0; i<nums.size(); i++){
            nums[i] = i & 0x1 ? sorted[--right] : sorted[--left];
        }
    }
};


class Solution_2 {
public:
    /*
    O(n)-time O(1)-space solution, no sort here.

    Find the kth smallest element, where k is the half the size (if size is even)
    or half the size+1 (if size is odd).

    Then do a three-way-partition, so that they can be split in two parts.
    Number in left parts <= those in right parts and the duplicates are around median.

    Then put the smaller half of the numbers on the even indexes,
    and the larger half on the odd indexes.
    Here iterate from the back of two halves,
    so that the duplicates between two parts can be split apart.

    According to:
    https://leetcode.com/discuss/77133/o-n-o-1-after-median-virtual-indexing
    https://discuss.leetcode.com/topic/38189/clear-java-o-n-avg-time-o-n-space-solution-using-3-way-partition
    */
    void wiggleSort(vector<int>& nums) {
        int mid = (nums.size()+1) / 2;
        auto midptr = nums.begin() + mid;
        nth_element(nums.begin(), midptr, nums.end());
        int mid_val = *midptr;

        vector<int> nums_p(nums);
        three_way_partition(nums_p, mid_val);
        int right = nums.size();
        for(int i=0; i<nums.size(); i++){
            nums[i] = i & 0x1 ? nums_p[--right] : nums_p[--mid];
        }
    }

    void three_way_partition(vector<int> &nums, int mid_val){
        int i=0, j=0, n=nums.size()-1;
        while(j<=n){
            if(nums[j] < mid_val){
                swap(nums[i++], nums[j++]);
            }
            else if(nums[j] > mid_val){
                swap(nums[j], nums[n--]);
            }
            else{
                j++;
            }
        }
    }
};

/*
[4, 5, 5, 6]
[1, 5, 1, 1, 6, 4]
[1, 3, 2, 2, 3, 1]
*/
