import java.util.*;

class Solution {
    class Process {
        int priority;
        int index;
        
        public Process(int priority, int index) {
            this.priority = priority;
            this.index = index;
        }
        
        public int getPriority() { return this.priority; }
        public int getIndex() { return this.index; }
    }
    
    public int solution(int[] priorities, int location) {
        Queue<Process> que = new LinkedList<>();
        PriorityQueue<Integer> max_que = new PriorityQueue<>(Collections.reverseOrder());
        
        for (int i = 0; i < priorities.length; i++) {
            que.offer(new Process(priorities[i], i));
            max_que.offer(priorities[i]);
        }
        
        int cnt = 1;
        while (true) {
            Process curProcess = que.poll();
            int max_priority = max_que.peek();
            
            if (curProcess.getPriority() == max_priority) {
                if (curProcess.getIndex() == location) {
                    break;
                }
                
                max_que.poll();
                         
                cnt++;
            } else {
                que.offer(curProcess);
            }
        }
        
        return cnt;
        
        
    }
}