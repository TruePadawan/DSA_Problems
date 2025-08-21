// Time Complexity : O(M * N)
class Solution {
    public int strStr(String haystack, String needle) {
        int index = -1;
        int i = 0;
        int j = 0;
        boolean processing = false;
        // Keep track of the next possible starting index
        int nextStart = -1;
        if (needle.length() > haystack.length()) {
            return index;
        }
        if (needle.length() == haystack.length() && !needle.equals(haystack)) {
            return index;
        }
        while (i < haystack.length() && j < needle.length()) {
            char h = haystack.charAt(i);
            char n = needle.charAt(j);
            if (haystack.charAt(i) == needle.charAt(0) && processing && nextStart == -1) {
                nextStart = i;
            }
            if (h != n) {
                // Start processing from the next possible starting index if it exists
                if (nextStart != -1) {
                    index = nextStart;
                    i = nextStart + 1;
                    j = 1;
                    nextStart = -1;
                    processing = true;
                } else {
                    i += 1;
                    j = 0;
                    index = -1;
                    processing = false;
                }
            } else {
                processing = true;
                if (index == -1) {
                    index = i;
                }
                i += 1;
                j += 1;
            }

        }
        // Processing is complete if the j-pointer got to the end
        if (j == needle.length()) {
            return index;
        }
        return -1;
    }
}