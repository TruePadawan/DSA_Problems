class Solution {
    String longest = "";

    public String longestPalindrome(String s) {
        for (int i = 0; i < s.length(); i++) {
            // Check for odd length palindrome
            int leftPtr = i;
            int rightPtr = i;
            while (leftPtr >= 0 && rightPtr < s.length()) {
                if (s.charAt(leftPtr) != s.charAt(rightPtr)) {
                    break;
                }
                String substr = s.substring(leftPtr, rightPtr + 1);
                if (substr.length() > longest.length()) {
                    longest = substr;
                }
                leftPtr -= 1;
                rightPtr += 1;
            }
            // Check for even length palindrome
            leftPtr = i;
            rightPtr = i + 1;
            while (leftPtr >= 0 && rightPtr < s.length()) {
                if (s.charAt(leftPtr) != s.charAt(rightPtr)) {
                    break;
                }
                String substr = s.substring(leftPtr, rightPtr + 1);
                if (substr.length() > longest.length()) {
                    longest = substr;
                }
                leftPtr -= 1;
                rightPtr += 1;
            }
        }
        return longest;
    }
}