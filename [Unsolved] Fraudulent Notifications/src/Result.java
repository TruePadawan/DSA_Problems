import java.util.List;

public class Result {

    /*
     * Complete the 'activityNotifications' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER_ARRAY expenditure
     *  2. INTEGER d
     */

    public static int activityNotifications(List<Integer> expenditure, int d) {
        int notifs = 0;
        int[] freqArr = new int[201];

        for (int day = 0; day < expenditure.size(); day++) {
            if (day >= d) {
                boolean isFraudulent = expenditure.get(day) >= 2 * getMedian(freqArr, d);
                if (isFraudulent) {
                    notifs += 1;
                }
                freqArr[expenditure.get(day - d)] -= 1;
            }
            freqArr[expenditure.get(day)] += 1;
        }
        return notifs;
    }

    public static double getMedian(int[] freqArr, int d) {
        int count = 0;
        double medianValue = -1;
        if (d % 2 != 0) {
            int medianIndex = (d / 2) + 1;
            for (int i = 0; i < freqArr.length; i++) {
                count += freqArr[i];
                if (count >= medianIndex) {
                    medianValue = i;
                    break;
                }
            }
        } else {
            int firstVal = -1;
            int firstIndex = d / 2;
            int secondIndex = firstIndex + 1;
            for (int i = 0; i < freqArr.length; i++) {
                count += freqArr[i];
                if (count >= firstIndex) {
                    firstVal = i;
                }
                if (count >= secondIndex) {
                    medianValue = (double) (firstVal + i) / 2;
                    break;
                }
            }
        }
        return medianValue;
    }
}