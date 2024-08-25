import java.util.*;

class Solution {

    public int[] solution(String[] genres, int[] plays) {
        HashMap<String, Integer> genreTotal = new HashMap<>();
        HashMap<String, List<Song>> genreMap = new HashMap<>();
        
        for (int i = 0; i < genres.length; i++) {
            genreTotal.put(genres[i], genreTotal.getOrDefault(genres[i], 0) + plays[i]);
            
            List<Song> songList = genreMap.getOrDefault(genres[i], new ArrayList<>());
            
            songList.add(new Song(i, plays[i]));
            genreMap.put(genres[i], songList);
        }
        
        // 재생횟수 많은 장르 순으로 정렬
        String[] sortedGenres = genreTotal.keySet().toArray(new String[0]);
        Arrays.sort(sortedGenres, (a, b) -> genreTotal.get(b) - genreTotal.get(a));
        
        List<Integer> result = new ArrayList<>();
        for (String genre : sortedGenres) {
            
            // 장르별 노래들 재생 횟수 내림차순 정렬
            List<Song> genreSongs = genreMap.get(genre);
            genreSongs.sort((a, b) -> b.play - a.play);
            
            // 가장 많이 재생된 2곡을 결과에 추가
            for (int i = 0; i < Math.min(2, genreSongs.size()); i++) {
                result.add(genreSongs.get(i).id);
            }
        }

        int[] answer = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }

        return answer;
    }
}

class Song {
    int id;
    int play;
    
    Song(int id, int play) {
        this.id = id;
        this.play = play;
    }
}