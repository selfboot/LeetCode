/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-06-30 16:15:49
 */

class Solution {
public:
    string addBinary(string a, string b) {
        string result = "";
        int c = 0, i = a.size() - 1, j = b.size() - 1;
        while(i>=0 || j>=0 || c==1){
            c += i >= 0 ? a[i --] - '0' : 0;
            c += j >= 0 ? b[j --] - '0' : 0;
            result = char(c % 2 + '0') + result;
            c /= 2;
        }
        return result;
    }
};


class Solution_2 {
public:
    string addBinary(string a, string b) {
        if(a.size()==0){
            return b;
        }
        if(b.size()==0){
            return a;
        }
        if(a[a.size()-1] == '1' && b[b.size()-1] == '1'){
            return addBinary(addBinary(
                string(a.begin(), a.end()-1), string(b.begin(), b.end()-1)), "1") + "0";
        }
        if(a[a.size()-1] == '0' && b[b.size()-1] == '0'){
            return addBinary(string(a.begin(), a.end()-1), string(b.begin(), b.end()-1)) + "0";
        }
        else{
            return addBinary(string(a.begin(), a.end()-1), string(b.begin(), b.end()-1)) + "1";
        }
    }
};

/*
"0"
"0"
"111000"
"111111111"
*/
