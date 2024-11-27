import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n, k, p, x;
    static int[] display = { 126, 48, 109, 121, 51, 91, 95, 112, 127, 123 };

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        p = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());

        System.out.println(solution());
    }

    public static int solution() {
        int count = 0;

        int[] currentDigit = numDigit(x);

        for (int i = 1; i <= n; i++) {
            if (i == x) continue;

            int[] targetDigit = numDigit(i);
            int totalChanges = 0;

            for (int j = 0; j < k; j++) {
                totalChanges += changeDisplayCnt(currentDigit[j], targetDigit[j]);
                if (totalChanges > p) break;
            }

            if (totalChanges <= p) {
                count++;
            }
        }

        return count;
    }

    public static int[] numDigit(int num) {
        int[] result = new int[k];
        for (int i = k - 1; i >= 0; i--) {
            result[i] = num % 10;
            num /= 10;
        }
        return result;
    }

    public static int changeDisplayCnt(int from, int to) {
        int diff = display[from] ^ display[to];
        return Integer.bitCount(diff);
    }
}
