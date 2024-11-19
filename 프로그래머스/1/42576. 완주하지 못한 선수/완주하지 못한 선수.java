import java.util.HashMap;
import java.util.Map;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> people = new HashMap<>();

        for (String name : participant) {
            people.put(name, people.getOrDefault(name, 0) + 1);
        }

        for (String name : completion) {
            people.put(name, people.get(name) - 1);
        }

        for (Map.Entry<String, Integer> entry : people.entrySet()) {
            if (entry.getValue() > 0) {
                return entry.getKey();
            }
        }

        return "";
    }
}