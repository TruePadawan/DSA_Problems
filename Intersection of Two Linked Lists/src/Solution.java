import java.util.Hashtable;

public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        Hashtable<ListNode, Boolean> nodes = new Hashtable<ListNode, Boolean>();
        while (headA != null || headB != null) {
            if (headA != null) {
                if (nodes.get(headA) != null) {
                    return headA;
                }
                nodes.put(headA, true);
                headA = headA.next;
            }
            if (headB != null) {
                if (nodes.get(headB) != null) {
                    return headB;
                }
                nodes.put(headB, true);
                headB = headB.next;
            }
        }
        return null;
    }
}