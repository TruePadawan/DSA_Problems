class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 1) return strs[0];
        StringBuilder longestPrefix = new StringBuilder();
        for (int i = 0; i < strs[0].length(); ++i) {
            char currentChar = strs[0].charAt(i);
            // Inner loop checks that all words have the same current prefix
            for (String word : strs) {
                if (i >= word.length() || word.charAt(i) != currentChar) {
                    return longestPrefix.toString();
                }
            }
            longestPrefix.append(currentChar);
        }
        return longestPrefix.toString();
    }
}