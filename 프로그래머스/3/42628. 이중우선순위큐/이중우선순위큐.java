import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        PriorityQueue<Integer> min_pq = new PriorityQueue<>();
        PriorityQueue<Integer> max_pq = new PriorityQueue<>((o1, o2) -> o2 - o1);
        int[] answer = new int[]{0, 0};
        
        for (String operation : operations) {
            String[] op = operation.split(" ");
            
            switch (op[0]) {
                case "I":
                    Integer value = Integer.parseInt(op[1]);
                    
                    min_pq.add(value);
                    max_pq.add(value);
                    
                    break;
                case "D":
                    if (op[1].equals("1")) {
                        Integer maxValue = max_pq.poll();
                        min_pq.remove(maxValue);
                    } else {
                        Integer minValue = min_pq.poll();
                        max_pq.remove(minValue);
                    }
                    break;
            }
        }
        
        if (!max_pq.isEmpty()) {
            answer[0] = max_pq.peek();
            answer[1] = min_pq.peek();
        }
        
        return answer;
    }
}