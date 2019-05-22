def josephus(items, k):
    i, result = 0, []
    while len(items) > 0:
        i = (i + k - 1) % len(items)
        result.append(items.pop(i))
    return result
	
