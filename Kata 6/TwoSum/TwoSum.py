'''
if target= 5

numbers=[1,2,3,7]

need return indxe=[1,2]

'''
def two_sum(nums, target):
    d = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in d:
            return [d[diff], i]
        d[num] = i
        
        