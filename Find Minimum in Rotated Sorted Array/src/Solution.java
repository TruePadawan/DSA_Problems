class Solution {
    public static int findMin(int[] nums) {
        /* Approach gotten from NeetCode
         */
        int l = 0;
        int r = nums.length - 1;
        int smallest = Integer.MAX_VALUE;
        while (l <= r) {
            int m = (l+r) / 2;
            smallest = Math.min(nums[m], smallest);

            // Is the middle pointer in the left or right partition?
            if (nums[m] >= nums[l]) {
                // I'm in the left partition, search right partition
                smallest = Math.min(nums[l], smallest);
                l = m + 1;
            } else {
                // I'm in the right partition, search left
                r = m - 1;
            }
        }
        return smallest;
    }
}