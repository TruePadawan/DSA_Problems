import java.util.HashMap;

class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int leftPtr = 0;
        int rightPtr = 0;
        int windowSize = 0;

        // Create a hash map for constant time operations (contains)
        HashMap<Character, Integer> charsCount = new HashMap<>(s1.length());
        HashMap<Character, Integer> charsCountCopy = new HashMap<>(s1.length());
        for (int i = 0; i < s1.length(); ++i) {
            char currentChar = s1.charAt(i);
            if (charsCount.containsKey(currentChar)) {
                charsCount.put(currentChar, charsCount.get(currentChar) + 1);
                charsCountCopy.put(currentChar, charsCount.get(currentChar));
            } else {
                charsCount.put(currentChar, 1);
                charsCountCopy.put(currentChar, 1);
            }
        }

        int nextStartingPoint = -1;
        while (windowSize < s1.length() && rightPtr < s2.length()) {
            char currentChar = s2.charAt(rightPtr);
            if (!charsCount.containsKey(currentChar) || charsCount.get(currentChar) == 0) {
                if (nextStartingPoint == -1) {
                    leftPtr = rightPtr;
                    rightPtr += 1;
                    leftPtr += 1;
                } else {
                    leftPtr = nextStartingPoint;
                    rightPtr = nextStartingPoint;
                }
                // handle resets
                charsCount = new HashMap<>(charsCountCopy);
                nextStartingPoint = -1;
            } else {
                if (nextStartingPoint == -1 && rightPtr > leftPtr) nextStartingPoint = rightPtr;
                rightPtr += 1;
                charsCount.put(currentChar, charsCount.get(currentChar) - 1);
            }
            windowSize = rightPtr - leftPtr;
        }
        return windowSize == s1.length();
    }
}