import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> pqScov = new PriorityQueue<>();
        
        for (int scov : scoville) {
            pqScov.add(scov);
        }
        
        int result = 0;
        while (pqScov.size() > 1) {
            if (pqScov.peek() >= K) return result;
            
            int firstScov = pqScov.poll();
            int secondScov = pqScov.poll();
            
            pqScov.add(mixScoville(firstScov, secondScov));
            result++;
        }
        
        if (pqScov.peek() >= K) return result;
        
        return -1;
    }
    
    public int mixScoville(int scoville1, int scoville2) {
        return scoville1 + (scoville2 * 2);
    }
}