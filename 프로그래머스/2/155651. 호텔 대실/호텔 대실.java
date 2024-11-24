import java.util.*;

class Solution {
    public int solution(String[][] book_time) {
        List<Time> bookTimes = new ArrayList<>();
        for (String[] time : book_time) {
            int start = strToTime(time[0]);
            int end = strToTime(time[1]);
            
            bookTimes.add(new Time(start, end));
        }
        
        bookTimes.sort(
            (t1, t2) -> t1.getStart() == t2.getStart() ? t1.getEnd() - t2.getEnd() : t1.getStart() - t2.getStart()
        );
        
        PriorityQueue<Time> pqTime = new PriorityQueue<>((t1, t2) -> t1.getEnd() - t2.getEnd());
        for (Time bookTime : bookTimes) {
            if (!pqTime.isEmpty() && pqTime.peek().getEnd() <= bookTime.getStart()) {
                pqTime.poll();
            }
            
            pqTime.add(bookTime);
        }
        
        return pqTime.size();
        
    }
    
    public int strToTime(String strTime) {
        String[] time = strTime.split(":");
        
        return Integer.parseInt(time[0]) * 3600 + Integer.parseInt(time[1]) * 60;
    }
    
    
    class Time {
        private int start;
        private int end;
        
        public Time(int start, int end) {
            this.start = start;
            this.end = end + 10 * 60;
        }
        
        public int getStart() { return this.start; }
        public int getEnd() { return this.end; }
    }
}