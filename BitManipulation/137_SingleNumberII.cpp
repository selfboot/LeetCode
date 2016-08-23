/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-08-23 09:54:56
 */

class Solution {
public:
    /*
    If you sum the ith bit of all numbers and mod 3,
    it must be either 0 or 1 due to the constraint of this problem
    where each number must appear either three times or once.
    This will be the ith bit of that "single number".
    */
    int singleNumber(vector<int>& nums) {
        int bits[32]={0};
        int ret = 0;
        for(int i=0; i<32; i++){
            for(auto n: nums){
                bits[i] += (n >> i) & 0x1;
            }
            bits[i] %= 3;
            ret |= bits[i] << i;
        }
        return ret;
    }
};

class Solution_2 {
public:
    /*
    Use two-bits represents the sum(should be 0/3, 1, 2) of all num's i-th bit.
    Twice-Once(the two bits): 00(0, 3)-->01(1)-->10(2)-->00(0, 3)
    Then we need to set rules for 'once' and 'twice' so that they act as we hopes.
        once = once ^ n & (~twice)
        twice = twice ^ n & (~once)

    Since each of the 32 bits follow the same rules,
    we can calculate them all at once.
    */
    int singleNumber(vector<int>& nums) {
        int once=0, twice=0;
        for(auto n: nums){
            once = (once ^ n) & (~twice);
            twice = (twice ^ n) & (~once);
        }
        return once;
    }
};

/*
[1]
[1,1,3,1]
[1,1,1,2,2,2,3,4,4,4]
[-2,-2,1,1,-3,1,-3,-3,-4,-2]
*/
