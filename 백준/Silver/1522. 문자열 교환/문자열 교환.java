import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String strAB = br.readLine();

        int aCnt = 0;
        for (int i = 0; i < strAB.length(); i++) {
            if (strAB.charAt(i) == 'a') aCnt++;
        }

        int bCnt = 0;
        for (int i = 0; i < aCnt; i++) {
            if (strAB.charAt(i) == 'b') bCnt++;
        }

        int answer = Integer.MAX_VALUE;
        for (int i = 0; i < strAB.length(); i++) {
            int insertIdx = (i + aCnt) % strAB.length();
            int deleteIdx = i;

            if (strAB.charAt(deleteIdx) == 'b') bCnt--;
            if (strAB.charAt(insertIdx) == 'b') bCnt++;

            answer = Math.min(answer, bCnt);
        }

        System.out.println(answer);
    }

}
