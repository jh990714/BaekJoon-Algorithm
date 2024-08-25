import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        // 트럭 다리에 올림
        // 다리를 건너는 트럭들 + 다음 트럭 무게가 weight보다 적으면 다음 트럭 올림 
        // 다리의 트럭 -> 길이만큼 que에 0으로 저장, 초마다 poll()
        
        int time = 0;
        int bridgeWeight = 0;
        int truckIndex = 0;
        Queue<Integer> bridge = new LinkedList<>();

        for (int i = 0; i < bridge_length; i++) {
            bridge.offer(0);
        }
        
        while (truckIndex < truck_weights.length) {
            time++;
            
            bridgeWeight -= bridge.poll();
            
            // 다음 트럭을 다리에 올릴 수 있을때
            if (weight >= bridgeWeight + truck_weights[truckIndex]) {
                bridge.add(truck_weights[truckIndex]);
                bridgeWeight += truck_weights[truckIndex];
                truckIndex++;
            } else {
                // 트럭이 다리에 오를 수 없으면 빈 공간(0) 추가
                bridge.offer(0);
            }
        }
        
        return time + bridge_length;
    }
}