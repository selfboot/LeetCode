/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-04 17:57:31
 */

class Solution {
public:
    /*
    Easy to find that power of 4 numbers have those 3 common features.
    First, greater than 0.
    Second, only have one '1' bit in their binary notation.
    Third, the only '1' bit should be locate at the odd location.
    */
    bool isPowerOfFour(int num) {
        // return num > 0 && (num & (num - 1)) == 0 && (num - 1) % 3 == 0;
        return num>0 && (num&(num-1))==0 && (num&0x55555555);
    }
};

/*
1
16
256
1000
*/
