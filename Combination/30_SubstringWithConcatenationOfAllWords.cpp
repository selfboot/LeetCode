/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-12 18:58:58
 */

class Solution {
public:
    // Easy to understand but slow.
    vector<int> findSubstring(string s, vector<string>& words) {
        int s_len = s.size();
        int w_len = words.size();
        if(s_len == 0 || w_len==0){
            return {};
        }

        int wl = words[0].size();
        int str_len = w_len * words[0].size();
        unordered_map<string, int> word_cnt;
        for(auto &w: words){
            word_cnt[w] += 1;
        }
        vector<int> ans;
        for(int i=0; i<s_len-str_len+1; i++){
            unordered_map<string, int> tmp_cnt;
            int j=0;
            while(j<w_len){
                string cur_word = s.substr(i+j*wl, wl);
                if(word_cnt.find(cur_word)==word_cnt.end()){
                    break;
                }
                else{
                    tmp_cnt[cur_word] ++;
                    if(tmp_cnt[cur_word] > word_cnt[cur_word]){
                        break;
                    }
                }
                j++;
            }
            if(j == w_len){
                ans.push_back(i);
            }
        }
        return ans;
    }
};


class Solution_2 {
public:
    /*
    Use hashmap and two point.

    Travel all the words combinations to maintain a slicing window.
    There are wl(word len) times travel, each time n/wl words:
    mostly 2 times travel for each word:
        one left side of the window, the other right side of the window
    So, time complexity O(wl * 2 * N/wl) = O(2N)
    Refer to:
    https://discuss.leetcode.com/topic/6617/an-o-n-solution-with-detailed-explanation
    */
    vector<int> findSubstring(string s, vector<string>& words) {
        int s_len = s.size();
        int total_cnt = words.size();
        if(s_len == 0 || total_cnt==0){
            return {};
        }

        int w_len = words[0].size();
        unordered_map<string, int> words_cnt;
        for(auto &w: words){
            words_cnt[w] ++;
        }

        vector<int> ans;
        for(int i=0; i<w_len; i++){
            int left=i, count=0;
            unordered_map<string, int> candidate_cnt;
            for(int j=i; j<=s_len-w_len; j+=w_len){
                string cur_str = s.substr(j, w_len);
                if(words_cnt.find(cur_str) != words_cnt.end()){
                    candidate_cnt[cur_str] ++;
                    count += 1;
                    if(candidate_cnt[cur_str] > words_cnt[cur_str]){
                        // A more word, advance the window left side possiablly
                        while(candidate_cnt[cur_str] > words_cnt[cur_str]){
                            string left_str = s.substr(left, w_len);
                            candidate_cnt[left_str] --;
                            left += w_len;
                            count --;
                        }
                    }
                    // come to a result
                    if(count == total_cnt){
                        ans.push_back(left);
                        candidate_cnt[s.substr(left, w_len)] --;
                        count --;
                        left += w_len;
                    }
                }
                else{
                    left = j+w_len;
                    candidate_cnt = {};
                    count = 0;
                }
            }
        }
        return ans;
    }
};


/*
""
[]
"barfoothefoobarman"
["foo", "bar"]
"barfoofoobarthefoobarman"
["bar","foo","the"]
*/
