import java.util.*;

public class Solution {

    public int solution(String begin, String target, String[] words) {
        if (!Arrays.asList(words).contains(target)) {
            return 0;
        }

        Map<String, List<String>> graph = createGraph(begin, words);

        return bfs(graph, begin, target);
    }

    private Map<String, List<String>> createGraph(String begin, String[] words) {
        Map<String, List<String>> graph = new HashMap<>();
        
        List<String> allWords = new ArrayList<>(Arrays.asList(words));
        allWords.add(begin);
        
        for (String word : allWords) {
            graph.put(word, new ArrayList<>());
            for (String otherWord : allWords) {
                if (canTransform(word, otherWord)) {
                    graph.get(word).add(otherWord);
                }
            }
        }

        return graph;
    }

    private int bfs(Map<String, List<String>> graph, String begin, String target) {
        Queue<WordNode> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        queue.offer(new WordNode(begin, 0));
        visited.add(begin);

        while (!queue.isEmpty()) {
            WordNode current = queue.poll();
            String currentWord = current.word;
            int currentStep = current.step;

            if (currentWord.equals(target)) {
                return currentStep;
            }

            for (String neighbor : graph.get(currentWord)) {
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    queue.offer(new WordNode(neighbor, currentStep + 1));
                }
            }
        }

        // target을 찾지 못한 경우 0을 반환
        return 0;
    }

    // canTransform 메서드: 두 단어가 한 글자 차이인지 확인하는 메서드
    private boolean canTransform(String word1, String word2) {
        int count = 0;
        for (int i = 0; i < word1.length(); i++) {
            if (word1.charAt(i) != word2.charAt(i)) {
                count++;
            }
            
            if (count > 1) return false;
        }
        return count == 1;
    }

    // WordNode 클래스: BFS 탐색에 사용할 노드를 표현
    class WordNode {
        String word;
        int step;

        WordNode(String word, int step) {
            this.word = word;
            this.step = step;
        }
    }
}
