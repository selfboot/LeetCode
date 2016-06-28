/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-06-28 16:15:41
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
    ListNode* rotateRight(ListNode* head, int k) {
        if(head==NULL || head->next==NULL){
            return head;
        }
        // Get the length of the linked list firstly.
        int length = 0;
        ListNode *len_scan = head;
        while(len_scan){
            length += 1;
            len_scan = len_scan->next;
        }

        k = k % length;
        if(k==0){
            return head;
        }

        // Get the rotated linked list's head.
        ListNode *new_tail = head;
        for(int i=0; i<length-1-k; i++){
            new_tail = new_tail -> next;
        }
        ListNode *new_head = new_tail->next;
        new_tail->next = NULL;

        // Go along the linked list to reach the original tail.
        ListNode *original_tail = new_head;
        while(original_tail and original_tail->next){
            original_tail = original_tail->next;
        }

        // Merge the two parts.
        original_tail->next = head;
        return new_head;
    }
};

/*
[]
0
[1,2,3,4,5]
0
[1,2,3,4,5]
3
[1,2,3,4,5]
9
[]
2
*/
