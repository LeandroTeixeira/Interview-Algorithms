def twoSum(nums: list[int], target: int) -> list[int]:
    if(len(nums) < 2):
        return []
    hash_map = dict()
    for index,value in enumerate(nums):
        x = target - value
        if x in hash_map.keys():
            return [index,hash_map[x]]
        else:
            hash_map [value] = index
    return []
        