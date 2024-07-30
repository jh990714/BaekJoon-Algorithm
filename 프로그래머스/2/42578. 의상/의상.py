def solution(clothes):
    clothes_type = {}
    
    for name, type in clothes:
        clothes_type[type] = clothes_type.get(type, 0) + 1
    
    result = 1
    for cnt in clothes_type.values():
        result *= (cnt + 1)
        
    return result - 1