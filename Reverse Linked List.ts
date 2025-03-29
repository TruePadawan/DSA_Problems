/*
* Traverse the list while current node is not null, for each node:
*   Point it its 'next' to the former node while keeping track of the original next
*   Move to the original next and do the same
*/
// Definition for singly-linked list.
class ListNode {
    val: number
    next: ListNode | null

    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}

function reverseList(head: ListNode | null): ListNode | null {
    let formerNode = null
    while (head !== null) {
        const originalNextNode = head.next
        head.next = formerNode
        formerNode = head
        head = originalNextNode
    }
    return formerNode
};