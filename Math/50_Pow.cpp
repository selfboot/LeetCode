/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-06-26 20:16:28
 */
class Solution {
public:
    double myPow(double x, int n) {
        // Simple recursively way.
        if(n == 0){
            return 1.0;
        }

        int half_abs = abs(n/2);
        if(n>0){
            double result = myPow(x*x, half_abs);
            if(n&0x1 == 1){
                result *= x;
            }
            return result;
        }
        else{
            double result = 1/myPow(x*x, half_abs);
            if(n&0x1 == 1){
                result *= 1/x;
            }
            return result;
        }
    }
};

class Solution_2{
public:
    double myPow(double x, int n) {
        /* Another way: shorter code.
         * According to: https://leetcode.com/problems/powx-n/
         * Important here.  Or if n == INT_MIN, it will overload.
         */
        long ln = n;
        if(ln==0){
            return 1.0;
        }
        if(ln<0){
            ln = -ln;
            x = 1/x;
        }
        return ln&0x1==1 ? x * myPow(x*x, ln/2) : myPow(x*x, ln/2);
    }
};

/*
8.88023
3
2.00000
-2147483648
2.2
-100
*/
