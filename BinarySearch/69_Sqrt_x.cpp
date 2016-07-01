/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-01 20:42:32
 */

class Solution {
public:
    int mySqrt(int x) {
        if(x < 2){
            return x;
        }
        int low = 0, high = x;
        while(low <= high){
            int mid = low + (high - low) / 2;
            // mid * mid will overflow when mid > sqrt(INT_MAX)
            if(x / mid >= mid  && x / (mid+1) < (mid+1)){
                return mid;
            }
            else if(x / mid < mid){
                high = mid - 1;
            }
            else{
                low = mid + 1;
            }
        }
        return -1; // Can'e be reached!
    }
};

class Solution_2{
public:
    int mySqrt(int x) {
        // Newton iterative method
        long ans = x;
        while(ans * ans > x){
            ans = (ans + x/ans) / 2;
        }
        return ans;
    }
};

/*
0
1
15
90
1010
*/
