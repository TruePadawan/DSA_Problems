// Symbol       Value
//  I             1
//  V             5
//  X             10
//  L             50
//  C             100
//  D             500
//  M             1000

/*
 * Loop through each symbol and add up its corresponding value
 * Special cases
 * If 'I' is encountered, and it is not the last symbol:
 *   If V is after it, add 4, skip V
 *   If X is after it, add 9, skip X
 * Do similar things for X and C
 * */

import java.util.HashMap;

class Solution {
    HashMap<Character, Integer> romanSymbols = new HashMap<>();

    Solution() {
        romanSymbols.put('I', 1);
        romanSymbols.put('V', 5);
        romanSymbols.put('X', 10);
        romanSymbols.put('L', 50);
        romanSymbols.put('C', 100);
        romanSymbols.put('D', 500);
        romanSymbols.put('M', 1000);
    }

    public int romanToInt(String s) {
        int result = 0;
        for (int i = 0; i < s.length(); ++i) {
            char symbol = s.charAt(i);
            boolean isLastSymbol = i == s.length() - 1;
            switch (symbol) {
                case 'I':
                    if (!isLastSymbol && s.charAt(i + 1) == 'V') {
                        result += 4;
                        i += 1;
                    } else if (!isLastSymbol && s.charAt(i + 1) == 'X') {
                        result += 9;
                        i += 1;
                    } else {
                        result += romanSymbols.get(symbol);
                    }
                    break;
                case 'X':
                    if (!isLastSymbol && s.charAt(i + 1) == 'L') {
                        result += 40;
                        i += 1;
                    } else if (!isLastSymbol && s.charAt(i + 1) == 'C') {
                        result += 90;
                        i += 1;
                    } else {
                        result += romanSymbols.get(symbol);
                    }
                    break;
                case 'C':
                    if (!isLastSymbol && s.charAt(i + 1) == 'D') {
                        result += 400;
                        i += 1;
                    } else if (!isLastSymbol && s.charAt(i + 1) == 'M') {
                        result += 900;
                        i += 1;
                    } else {
                        result += romanSymbols.get(symbol);
                    }
                    break;
                default:
                    result += romanSymbols.get(symbol);
                    break;
            }
        }
        return result;
    }
}