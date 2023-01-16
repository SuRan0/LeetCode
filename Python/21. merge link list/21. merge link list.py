class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2


l1_1 = ListNode(1)
l1_2 = ListNode(2)
l1_3 = ListNode(4)
l1_1.next = l1_2
l1_2.next = l1_3

l2_1 = ListNode(1)
l2_2 = ListNode(3)
l2_3 = ListNode(4)
l2_1.next = l2_2
l2_2.next = l2_3

l3 = mergeTwoLists(l1_1, l2_1)
result = []
while(l3 != None):
    result.append(l3.val)
    l3 = l3.next
print(result)
