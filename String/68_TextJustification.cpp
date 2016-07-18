/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-18 20:48:50
 */

class Solution {
public:
    /*
    Straightforward solution for the problem

    Once you determine that there are only k words that can fit on a given line,
    you know what the total length of those words is cur_letters.
    Then the rest are spaces, and there are L = (maxWidth - cur_letters) of spaces.

    The trick here is to use mod operation to manage the spaces.
    The "or 1" part is for dealing with the edge case len(cur) == 1.

    Refer to:
    https://discuss.leetcode.com/topic/25970/concise-python-solution-10-lines
    https://discuss.leetcode.com/topic/4189/share-my-concise-c-solution-less-than-20-lines
    */
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> ans, cur_words;
        int cur_letters = 0;
        for(auto &w : words){
            if(cur_words.size() + cur_letters + w.size() > maxWidth){
                int pad_space_cnt = maxWidth - cur_letters;
                for(int i=0; i<pad_space_cnt; i++){
                    cur_words[i%((cur_words.size() > 1 ? cur_words.size()-1 : 1)) ] += " ";
                }
                string new_line = "";
                for(auto s : cur_words){
                    new_line += s;
                }
                ans.push_back(new_line);
                cur_words = {};
                cur_letters = 0;
            }

            cur_letters += w.size();
            cur_words.push_back(w);
        }
        if(cur_words.size() > 0){
            string new_line = cur_words[0];
            for(int i=1; i<cur_words.size(); i++){
                new_line += " " + cur_words[i];
            }
            new_line += string(maxWidth - new_line.size(), ' ');
            ans.push_back(new_line);
        }
        return ans;
    }
};

/*
["a"]
1
[""]
2
["This", "is", "an", "example", "of", "text", "justification."]
15
["This", "is", "an", "example", "of", "text", "justification."]
16
["This", "is", "an", "example", "of", "text", "justification."]
20
["What","must","be","shall","be."]
12
*/
