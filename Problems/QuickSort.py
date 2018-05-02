arr = [3,5,2,6,8,4,5,8,3,1,10,3,5,9]

res = []
def quickSort(arr,i,j):
	res.append(arr[:])
	left = i
	right = j
	if left >= right:
		return
	tmp = arr[left]
	while left < right:
		while left < right and arr[right] >= tmp:
			right -= 1
		arr[left] = arr[right]
		while left < right and arr[left] <= tmp:
			left += 1
		arr[right] = arr[left]
	arr[left] = tmp
	quickSort(arr,i,left-1)
	quickSort(arr,left+1,j)

quickSort(arr,0,len(arr)-1)
for vec in res:
	print(vec)