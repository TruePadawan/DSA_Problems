import java.util.ArrayList;
import java.util.List;

// O(M+N) Approach
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int i = 0;
        int j = 0;
        List<Integer> res = new ArrayList<>();
        while (i < nums1.length || j < nums2.length) {
            if (i < nums1.length && j < nums2.length) {
                if (nums1[i] <= nums2[j]) {
                    res.add(nums1[i]);
                    i += 1;
                } else {
                    res.add(nums2[j]);
                    j += 1;
                }
            } else {
                if (i < nums1.length) {
                    res.add(nums1[i]);
                    i += 1;
                } else {
                    res.add(nums2[j]);
                    j += 1;
                }
            }
        }
        if (res.size() % 2 == 0) {
            int a = res.size() / 2;
            int b = a - 1;
            return (double) (res.get(a) + res.get(b)) / 2;
        } else {
            return res.get(res.size() / 2);
        }
    }
}