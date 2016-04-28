/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-28 13:58:30
 */

class Solution {
public:
    int countDigitOne(int n)
    {
        if(n<=0) return 0;
        long long count = 1;
        while(n){
            if(n<10){
                break;
            }
            int digit = n % 10;
            n /= 10;
            count += n;
            if(digit == 0)  count -= 1;
            count += countDigitOne(n-1) * 10;

            // 最后一行中数组1出现的次数
            while(n){
                if(n%10==1) count += digit+1;
                n /= 10;
            }
        }
        return count;
    }
};

/*
-1
6
12
234545
*/
