/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-05-04 22:03:09
 */

class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0|| (x!=0 &&x%10==0)) return false;
        int sum=0;
        while(x>sum)
        {
            sum = sum*10+x%10;
            x = x/10;
        }
        return (x==sum)||(x==sum/10);
    }
};

/*
9
10
-2147483648
32023
320023
98765432123456789
*/
