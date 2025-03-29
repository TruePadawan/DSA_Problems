// Approach 1:
// Keep track of carried over values (carry_over)
// Create a resultant list which will be returned, it won't move from its root
// Create a copy node which will be used for appending elements to the list

// We'll have to loop as long as the current node of both lists are not None:
//     Get value from node that isn't None
//     sum up with carry_over
//     if sum >= 10:
//         we'll be appending the -1th value to our resultant list
//         carry_over will equal the 0th value
//     else:
//         we'll be appending the sum to the resultant list
//         carry_over = 0

//     move the copy to its next node
//     move both lists to their next node    
// Submit resultant list


// Definition for singly-linked list.
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    const rootNode = new ListNode()
    let workerNode = rootNode
    let carryOverValue = 0

    while (l1 !== null || l2 !== null) {
        const l1Value = l1?.val ?? 0
        const l2Value = l2?.val ?? 0
        const sum = l1Value + l2Value + carryOverValue
        
        if (sum >= 10) {
            carryOverValue = 1
            workerNode.val = sum - 10
        } else {
            carryOverValue = 0
            workerNode.val = sum
        }


        l1 = l1?.next ?? null
        l2 = l2?.next ?? null

        const atLastLoop = l1 == null && l2 == null
        if (atLastLoop) {
            workerNode.next = carryOverValue > 0 ? new ListNode(carryOverValue) : null
        } else {
            workerNode.next = new ListNode()
            workerNode = workerNode.next
        }
    }
    return rootNode
};