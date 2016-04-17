/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-17 17:26:46
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
    // Recursively reverse
    ListNode* reverseList(ListNode* head) {
        if(head==NULL || head->next == NULL){
            return head;
        }
        ListNode *reversed_head = reverseList(head->next);
        head->next->next = head;
        head->next = NULL;
        return reversed_head;
    }
};

class Solution_2 {
public:
    // Itratively reverse
    ListNode* reverseList(ListNode* head) {
        ListNode *new_head = NULL;
        while(head!=NULL){
            ListNode *next_node = head->next;
            head->next = new_head;
            new_head = head;
            head = next_node;
        }
        return new_head;
    }
};

/*
[]
[1]
[1,2]
[1,2,3,4,5]
*/
