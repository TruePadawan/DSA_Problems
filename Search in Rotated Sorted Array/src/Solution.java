class Solution {
    public int search(int[] nums, int target) {
        int l = 0;
        int r = nums.length - 1;
        while (l <= r) {
            int m = (l + r) / 2;
            if (nums[m] == target) return m;
            if (nums[m] >= nums[l]) {
                // In left partition
                if (target >= nums[l] && target <= nums[m]) {
                    // Search left partition
                    r = m - 1;
                } else {
                    l = m + 1;
                }
            } else {
                // In right partition
                if (target >= nums[m] && target <= nums[r]) {
                    // Search right partition
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            }
        }
        return -1;
    }
}