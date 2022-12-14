def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    node = dummy
    remaining = 0

    while l1 or l2:
        if not l1:
            node.next = l2
            l1 = ListNode(0)
        if not l2:
            node.next = l1
            l2 = ListNode(0)

        #
        remaining += l1.val + l2.val
        node.next = ListNode(remaining % 10)
        remaining = remaining // 10

        node = node.next
        l1 = l1.next
        l2 = l2.next

    if remaining:
        node.next = ListNode(remaining)

    return dummy.next