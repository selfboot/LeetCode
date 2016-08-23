/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-08-23 15:09:48
 */


class Solution {
public:
    /* Dynamic Programming.
    A very good explanation come with thinking process is here:
    https://leetcode.com/discuss/71354/share-my-thinking-process

    States definition:
        buy[i]: The maxProfit for any sequence end with buy in pre i days.
        sell[i]: The maxProfit for any sequence end with sell in pre i days.
    Transition function (price is the price of day i):
        buy[i] = max(buy[i-1], sell[i-2] - price)
        sell[i] = max(sell[i-1], buy[i-1] + price)
    To get buy[i](sell[i] is the same), there are two possibilities:
        1. No transaction on day i, then buy[i] = buy[i-1]
        2. Buy stock on day i, last sell must berofe i-1 day,
           then buy[i] = sell[i-2] - price
    */
    int maxProfit(vector<int>& prices) {
        size_t len = prices.size();
        if(len <2 ){
            return 0;
        }
        int pre_buy=-prices[0], buy=0, pre_sell=0, sell=0;
        for(size_t i=1; i<len; i++){
            // Here pre_sell is euqal sell[i-2], sell is equal sell[i-1]
            buy = max(pre_buy, pre_sell-prices[i]);
            pre_sell = sell;
            sell = max(pre_sell, pre_buy+prices[i]);
            pre_buy = buy;
        }
        return sell;
    }
};

/*
[]
[1,2,3,0,2]
[1,2,5,0,2]
[1,2,5,0,8]
*/
