import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int n;

    public static void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            int[] answer = new int[2];
            answer[0] = Integer.MAX_VALUE;
            answer[1] = -1;

            String word = br.readLine();
            int k = Integer.parseInt(br.readLine());

            int[] alpa = new int[26];
            for (int j = 0; j < word.length(); j++) {
                alpa[word.charAt(j) - 'a']++;
            }

            for (int j = 0; j < word.length(); j++) {
                if (alpa[word.charAt(j) - 'a'] < k) continue;

                int cnt = 0;
                for (int l = j; l < word.length(); l++) {
                    if (word.charAt(j) == word.charAt(l)) cnt++;

                    int length = l - j + 1;
                    if (cnt == k) {
                        answer[0] = Math.min(answer[0], length);
                        answer[1] = Math.max(answer[1], length);

                        break;
                    }
                }
            }
            
            if (answer[0] == Integer.MAX_VALUE || answer[1] == -1) {
                System.out.println(-1);
            } else {
                System.out.println(answer[0] + " " + answer[1]);
            }
        }
    }
    public static void main(String[] args) throws IOException {
        solution();
    }
}