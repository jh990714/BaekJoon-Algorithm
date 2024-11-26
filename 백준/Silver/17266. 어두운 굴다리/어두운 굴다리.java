import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int m;
    static int[] x;

    public static int solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());
        x = new int[m];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            x[i] = Integer.parseInt(st.nextToken());
        }

        return binarySearch();
    }

    public static int binarySearch() {
        int left = 0;
        int right = n;
        int result = n;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (isCheck(mid)) {
                result = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return result;
    }

    public static boolean isCheck(int h) {
        int covered = 0;

        for (int point : x) {
            if (point - h > covered) return false;

            covered = Math.max(covered, point + h);
        }

        return covered >= n;
    }

    public static void main(String[] args) throws IOException {
        System.out.println(solution());
    }
}