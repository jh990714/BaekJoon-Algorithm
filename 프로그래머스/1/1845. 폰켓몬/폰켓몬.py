def solution(nums):
    max_select_cnt = len(nums) // 2
    nums_set = set(nums)
    
    return min(max_select_cnt, len(nums_set))