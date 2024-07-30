def solution(genres, plays):
    total_plays = {}
    gen_nums = {}
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        total_plays[genre] = total_plays.get(genre, 0) + play
        if genre not in gen_nums:
            gen_nums[genre] = []
        gen_nums[genre].append((play, i))
        
    sorted_genres = sorted(total_plays.items(), key=lambda x: x[1], reverse=True)
    
    album = []
    for genre, _ in sorted_genres:
        sorted_gen_nums = sorted(gen_nums[genre], key=lambda x: (-x[0], x[1]))
        album.extend([num for _, num in sorted_gen_nums[:2]])
        
    return album
        
        