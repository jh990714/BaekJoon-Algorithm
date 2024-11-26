import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int[] x;
    static int[] answer;

    public static void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        x = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            x[i] = Integer.parseInt(st.nextToken());
        }

        answer = new int[n];
        for (int i = 0; i < n; i++) {
            answer[i] = Integer.MAX_VALUE;
        }

        for (int i = 0; i < n; i++) {
            int idx = findIndex(i + 1, x[i] + 1);

            answer[idx] = i + 1;
        }

        for (int i = 0; i < n; i++) {
            System.out.print(answer[i] + " ");
        }
        System.out.println();
    }

    public static int findIndex(int idx, int value) {
        int cnt = 0;

        for (int i = 0; i < n; i++) {
            if (answer[i] > idx) cnt++;
            if (cnt == value) return i;
        }

        return -1;

    }
    public static void main(String[] args) throws IOException {
        solution();
    }
}