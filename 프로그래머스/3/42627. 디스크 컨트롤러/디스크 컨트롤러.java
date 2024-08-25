import java.util.*;
/*
    현재시간 - 요청시간 + 작업기간
*/
class Solution {
    public int solution(int[][] jobs) {
        // 작업 안하고 있을때 -> 먼저 들어온거 실행
        // 작업 종료후 다음 작업 -> 작업기간이 짧은거
        int result = 0;
        int time = 0;
        int idx = 0;
        
        Arrays.sort(jobs, (a, b) -> a[0] - b[0]);
        
        PriorityQueue<int[]> pqJobs = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        while (!pqJobs.isEmpty() || idx < jobs.length) {
            // jobs에서 현재 시간보다 작거나 같은 거 추가
            while (idx < jobs.length && time >= jobs[idx][0]) {
                pqJobs.offer(jobs[idx]);
                idx++;
            }
            
            if (pqJobs.isEmpty()) {
                time = jobs[idx][0];
                continue;
            }
            
            int[] job = pqJobs.poll();
            result += (time - job[0] + job[1]);
            time += job[1];
        }
        
        return result / jobs.length;
    }
}