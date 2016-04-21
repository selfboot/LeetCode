/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-21 11:18:48
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
    /*
    Two pointers: one go 1 step, another one go 2 steps every time.
    Then if the list has a cycle, fast one will meet the slow one absolutely.
    Prove as follows:
    1. If has a circle
        Assume there are m nodes that not in cycle, and then k nodes in cycle.
        And slow one now go m+i nodes, fast one go 2m + 2i nodes whitout doubt.
        So, slow one in the i's node of the circle, and fast one m+2i
        That's say, fast one goes m+i steps more than slow one.
        As the nodes keep going,
        i grows so (m+i) mode k == 0, then fast and slow meet here.
    2. If not:
        fast one will meet None node.
    */
    bool hasCycle(ListNode *head) {
        ListNode* fast = head;
        ListNode* slow= head;
        while(fast && fast->next){
            fast = fast->next->next;
            slow = slow->next;
            if(fast==slow){
                return true;
            }
        }
        return false;
    }
};
