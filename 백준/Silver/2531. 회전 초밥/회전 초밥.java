import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int d;
    static int k;
    static int c;
    static int[] belt;
    static int[] sushi;

    public static void solution() throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        
        belt = new int[n];
        for (int i = 0; i < n; i++) {
            belt[i] = Integer.parseInt(br.readLine());
        }

        sushi = new int[d+1];
        sushi[c] = 1;
        int cnt = 1;
        for (int i = 0; i < k; i++) {
            if (sushi[belt[i]]++ == 0) cnt++;
        }

        int answer = cnt;
        for (int i = 0; i < n; i++) {
            int deleteIdx = belt[i];
            if (--sushi[deleteIdx] == 0) cnt--;

            int insertIdx = belt[(i + k) % n];
            if (sushi[insertIdx]++ == 0) cnt++;

            answer = Math.max(answer, cnt);
        }

        System.out.println(answer);
    }
    public static void main(String[] args) throws IOException {
        solution();
    }
}