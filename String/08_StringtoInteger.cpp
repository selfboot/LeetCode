/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-08-21 09:10:58
 */

class Solution {
public:
    int myAtoi(string str){
        /*
        We need to handle four cases:

        1. discards all leading whitespaces
        2. sign of the number
        3. overflow
        4. invalid input
        */
        const int len = str.size();

        int i=0;
        // Skip starting whitespace as many as possible.
        while (str[i]==' ' && i<len) i++;

        int sign = 1;
        // Read plus or minus sign.
        if(str[i] == '+') i++;
        else if(str[i] == '-'){
            i++;
            sign = -1;
        }

        int num = 0;
        for(; i<len; i++){
            if(str[i] < '0' || str[i] > '9'){
                break;
            }
            if(num > INT_MAX/10 || (num == INT_MAX / 10 && (str[i]-'0') > INT_MAX % 10)){
                return sign == -1 ? INT_MIN : INT_MAX;
            }
            num = num * 10 + str[i] - '0';
        }

        return num * sign;
    }
};

/*
""
"  12a"
"  a12"
"  +12"
"  +-12"
"2147483648"
"-2147483648"
*/
