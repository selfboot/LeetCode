/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-04 12:20:16
 */

class Solution {
public:
    string reverseVowels(string s) {
        long left = 0, right = s.size()-1;
        set<char> all_vowels = {'a', 'A', 'e', 'E', 'i',
                                'I', 'o', 'O', 'u', 'U'};

        while(left < right){
            if(all_vowels.find(s[left])!=all_vowels.end() && all_vowels.find(s[right])!=all_vowels.end()){
                swap(s[left], s[right]);
                left += 1;
                right -= 1;
            }
            else if(all_vowels.find(s[left])!=all_vowels.end()){
                right -= 1;
            }
            else if(all_vowels.find(s[right])!=all_vowels.end()){
                left += 1;
            }
            else{
                left += 1;
                right -= 1;
            }
        }
        return s;
    }
};


class Solution_2 {
public:
    // Super clean C++ solution using find_first_of and find_last_of
    // According to:
    // https://discuss.leetcode.com/topic/43452/super-clean-c-solution-using-find_first_of-and-find_last_of
    string reverseVowels(string s) {
        int i = 0, j = s.size() - 1;
        while (i < j) {
            i = s.find_first_of("aeiouAEIOU", i);
            j = s.find_last_of("aeiouAEIOU", j);
            if (i < j) {
                swap(s[i++], s[j--]);
            }
        }
        return s;
    }
};

/*
""
"hello"
"leetcode"
"Administrator"
*/
