/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-10 10:55:05
 */

class Solution {
public:
    /* Just according to:
     * https://discuss.leetcode.com/topic/31012/7-line-consice-o-kn-c-solution
     */
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        vector<int> index(primes.size(), 0), ugly_numbers(n, INT_MAX);
        ugly_numbers[0] = 1;
        for(int i=1; i<n; i++){
            for(int j=0; j<primes.size();j++){
                ugly_numbers[i]=min(ugly_numbers[i], ugly_numbers[index[j]]*primes[j]);
            }
            for(int j=0; j<primes.size();j++){
                index[j] += (ugly_numbers[i]==ugly_numbers[index[j]]*primes[j]);
            }
        }
        return ugly_numbers[n-1];
    }
};

/*
2
[2,3,5]
100
[2,3,5,7,11]
5
[2,3,5,7,11,13,17,19]
*/
