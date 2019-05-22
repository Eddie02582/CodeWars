'''
Examples
[1, 3, 4, 5], 7        ==> None  # n is more than the size of the list
[4, 3, 4, 5], 4        ==> None  # 4th smallest integer doesn't exist
[45, -10, 4, 5, 4], 4  ==> 45    # 4th smallest integer is 45

'''

# Timeout.....
#Time 11292ms
def nth_smallest(arr, n):
    return None if n> len(set(arr)) else sorted(set(arr))[n-1]
	
print nth_smallest([14, 12, 46, 34, 334], 3)