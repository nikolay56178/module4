def insert_sort(mas):
	n=len(mas)
	for i in range(1,n):
		for j in range(i,0,-1):
			if mas[j]<mas[j-1]:
				mas[j],mas[j-1]=mas[j-1],mas[j]
			else:
				break
	return mas
	
massive=[1,3,22,-16,44,4,-1,99]


print(insert_sort(massive))