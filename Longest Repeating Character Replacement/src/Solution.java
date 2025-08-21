import java.util.HashSet;
import java.util.Set;

/**
 * Using a sliding window technique, create a window that contains the same letter
 * The window increases when the next char is that same letter or not and we use one k to make
 */
class Solution {
    public static Set<Character> getCharSet(String s) {
        Set<Character> set = new HashSet<>();
        if (s == null) return set;
        for (int i = 0; i < s.length(); i++) {
            set.add(s.charAt(i));
        }
        return set;
    }

    public int characterReplacement(String s, int k) {
        HashSet<Character> charSet = new HashSet<Character>(getCharSet(s));
        for (char character : charSet) {
            int replacements = 0;
            int i = 0, j = 0;
            while (j < s.length()) {
                if (i == j & s.charAt(i) != character) {
                    i += 1;
                } else if (s.charAt(j) != character) {

                    replacements += 1;
                }
                j += 1;
            }
        }
        return 0;
    }
}