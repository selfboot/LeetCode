/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-02 17:09:34
 */


class Solution {
public:
    /*
    Firstly, calculate the carry.
    then calculate sum of a and b without thinking the carry.
    Finally add sum(without carry) and carry.
    */
    int getSum(int a, int b) {
        if(b==0){
            return a;
        }
        return getSum(a^b, (a&b)<<1);
    }
};


class Solution_2 {
public:
    int getSum(int a, int b) {
        while(b != 0){
            int carry_in = (a & b) << 1;
            int add_two = a ^ b;
            a = add_two;
            b = carry_in;
        }
        return a;
    }
};


"""
0
1
-3
5
12
10000098
-8
-12
"""
