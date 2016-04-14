/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-14 09:58:46
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *first = head;
        // Let the first pointer goto n+1'th node.
        int steps = 0;
        while(first){
            if(steps == n+1){
                break;
            }
            first = first->next;
            steps += 1;
        }

        // the node to be removed is the head node.
        if(steps < n+1){
            return head->next;
        }

        ListNode *second = head;
        while(first){
            second = second->next;
            first = first->next;
        }
        second->next = second->next->next;
        return head;
    }
};

/*
[1]
1
[1,2,3,4,5,6,7,8]
5
[1,2,3,4,5,6,7,8]
8
*/
