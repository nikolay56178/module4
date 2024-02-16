def bin_search(data,elem):
	low=0
	high= len(data)-1

	while low <= high:
		middle = (low+high)//2
		if data[middle]==elem:
			return middle
		elif data[middle]>elem:
			high=middle-1
		else:
			low = middle+1
	return -1

calendar=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
our_day=11
print(bin_search(calendar,our_day))