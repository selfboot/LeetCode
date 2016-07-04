/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-04 11:46:49
 */

class Solution {
public:
    bool isPerfectSquare(int num) {
        int low=0, high=num;
        while(low <= high){
            // long type to avoid overflow.
            long mid = (high-low) / 2 + low;
            long product = mid * mid;
            if(num == product){
                return true;
            }
            else if(product > num){
                high = mid - 1;
            }
            else{
                low = mid + 1;
            }
        }
        return false;
    }
};


class Solution_2 {
public:
    // Truth: A square number is 1+3+5+7+...  Time Complexity O(sqrt(N))
    bool isPerfectSquare(int num) {
        int i = 1;
        while(num>0){
            num -= i;
            i += 2;
        }
        return num == 0;
    }
};


class Solution_3 {
public:
    // Newton Method.  Time Complexity is close to constant.
    // According to: https://en.wikipedia.org/wiki/Newton%27s_method
    bool isPerfectSquare(int num) {
        long val = num;
        while(val * val > num){
            val = (val + num/val) / 2;
        }
        long ans = val * val;
        return ans == num;
    }
};

/*
0
1
121
12321
2147483647
*/
