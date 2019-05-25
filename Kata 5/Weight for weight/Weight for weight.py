def order_weight2(strng):
	s=strng.split()
	s.sort(key=lambda x: (sum(int(n) for n in x),x))
	return " ".join(s)


def order_weight(strng):
	return " ".join(sorted(strng.split(),key=lambda x: (sum(int(n) for n in x),x)))



#"2000 103 123 4444 99"
print (order_weight("56 65 74 100 99 68 86 180 90"))