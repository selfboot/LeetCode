/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-20 11:28:51
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    // Refer to:
    // https://leetcode.com/discuss/17278/accepted-shortest-explaining-algorithm-comments-improvements
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *p1 = headA;
        ListNode *p2 = headB;
        while(p1!=p2){
            p1 = (p1==NULL ? headB : p1->next);
            p2 = (p2==NULL ? headA : p2->next);
        }
        return p1;
    }
};

