#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
#include <crtdbg.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* merge = nullptr;
        ListNode* merge_head = nullptr;
        ListNode* merge_next = nullptr;

        if (list1 == nullptr) return list2;
        if (list2 == nullptr) return list1;

        if (list1->val < list2->val)
        {
            merge = list1;
            list1 = list1->next;
        }
        else
        {
            merge = list2;
            list2 = list2->next;
        }

        merge_head = merge;

        while (true)
        {
            if (list1 == nullptr)
            {
                merge_next = list2;
                merge->next = merge_next;
                merge = merge->next;
                break;
            }

            if (list2 == nullptr)
            {
                merge_next = list1;
                merge->next = merge_next;
                merge = merge->next;
                break;
            }

            if (list1->val < list2->val)
            {
                merge_next = list1;
                list1 = list1->next;
            }
            else
            {
                merge_next = list2;
                list2 = list2->next;
            }

            merge->next = merge_next;
            merge = merge->next;
        }

        return merge_head;
    }
};

void Free(ListNode* list)
{
    ListNode* head = list;
    ListNode* next = list->next;

    while (head != nullptr)
    {
        delete head;
        head = next;

        if (next != nullptr)
            next = next->next;
    }
}

int main()
{
    _CrtSetDbgFlag(_CRTDBG_ALLOC_MEM_DF | _CRTDBG_LEAK_CHECK_DF);

    Solution s;
    ListNode* list1 = new ListNode(1, new ListNode(2, new ListNode(4)));
    ListNode* list2 = new ListNode(1, new ListNode(3, new ListNode(4)));

    ListNode* node = s.mergeTwoLists(list1, list2);

    Free(node);

    return 0;
}