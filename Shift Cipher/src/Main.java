import java.util.Scanner;

public class Main {
    public static void shiftCipher(String message, int shift) {
        String[] words = message.split("\\s+");
        boolean toBeEncrypted = false;

        // check if contains exact word "the"
        for (String word : words) {
            if (word.equals("the")) {
                toBeEncrypted = true;
                break;
            }
        }

        StringBuilder result = new StringBuilder();
        for (int i = 0; i < message.length(); ++i) {
            String letter = message.substring(i, i+1);

            if (letter.equals(" ")) {
                result.append(letter);
            } else {
                int charIndex = letter.charAt(0) - 'a';
                if (toBeEncrypted) {
                    int newIndex = charIndex - shift;
                    if (newIndex < 0) {
                        newIndex += 26;
                    }
                    char encryptedLetter = (char) ('a' + newIndex);
                    result.append(encryptedLetter);
                } else {
                    int newIndex = charIndex + shift;
                    if (newIndex > 25) {
                        newIndex -= 26;
                    }
                    char decryptedLetter = (char) ('a' + newIndex);
                    result.append(decryptedLetter);
                }
            }
        }
        System.out.println(result.toString());
    }
    public static void main (String [] args) throws java.lang.Exception {
        Scanner in = new Scanner(System.in);
        try (in) {
            int N = Integer.parseInt(in.nextLine().trim());
            for (int i = 0; i < N; i++) {
                int shift = Integer.parseInt(in.nextLine().trim());
                String message = in.nextLine().trim();
                shiftCipher(message, shift);
            }
        }

    }
}
