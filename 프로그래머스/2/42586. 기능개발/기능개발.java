import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        Queue<Integer> que = new LinkedList<>();
        List<Integer> answer = new ArrayList<>();
        
        for (int i = 0; i < progresses.length; i++) {
            int days = (int) Math.ceil((100.0 - progresses[i]) / speeds[i]);

            if (!que.isEmpty() && que.peek() < days) {
                answer.add(que.size());
                que.clear();
            }

            que.add(days);
        }
        
        answer.add(que.size());
        
        return answer.stream().mapToInt(i -> i).toArray();
        
    }
}