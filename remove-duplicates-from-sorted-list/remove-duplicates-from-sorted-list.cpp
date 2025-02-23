/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

//1->1->2
//Output: 1->2

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* tmp = head;
        while(tmp != nullptr && tmp->next != nullptr) {
            if (tmp->val == tmp->next->val) {
                tmp->next = tmp->next->next;
            } else {
                tmp = tmp->next;
            }
        }
        return head;
    }
};