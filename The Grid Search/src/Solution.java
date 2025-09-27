import java.util.List;

class Solution {
    public static String gridSearch(List<String> G, List<String> P) {
        for (int i = 0; i < G.size(); i++) {
            String row = G.get(i);
            int firstPatternIndex = row.indexOf(P.get(0));
            while (firstPatternIndex != -1) {
                // Check if the full pattern is in this row and col
                if (verify(i, firstPatternIndex, G, P)) {
                    return "YES";
                } else {
                    int patternWidth = P.get(0).length();
                    firstPatternIndex = row.indexOf(P.get(0), firstPatternIndex + patternWidth);
                }
            }
        }
        return "NO";
    }

    public static boolean verify(int row, int colStart, List<String> grid, List<String> pattern) {
        if (grid.size() - row < pattern.size()) return false;
        int colEnd = colStart + pattern.get(0).length();
        for (int i = 0; i < pattern.size(); ++i) {
            String gridSubstr = grid.get(row + i).substring(colStart, colEnd);
            if (!gridSubstr.equals(pattern.get(i))) return false;
        }
        return true;
    }
}
