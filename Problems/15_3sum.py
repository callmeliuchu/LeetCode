

def swap(arr,i,j):
	arr[i],arr[j] = arr[j],arr[i]

def f(arr,index):
	if index == len(arr):
		print(arr)
	for i in range(index,len(arr)):
		swap(arr,i,index)
		f(arr,index+1)
		swap(arr,i,index)


def f1(n,m,index,arr,res):
	if len(arr) == m:
		res.append(arr[:])
		return
	for i in range(index,n):
		arr.append(i)
		f1(n,m,i+1,arr,res)
		arr.pop()

def ff(n,m):
	res = []
	f1(4,2,0,[],res)
	return res

def f2(m,index,inputArr,arr,res):
	if len(arr) == m and arr not in res and sum(arr)==0:
		res.append(arr[:])
	for i in range(index,len(inputArr)):
		arr.append(inputArr[i])
		f2(m,i+1,inputArr,arr,res)
		arr.pop()



res = []
f2(3, 0,sorted([-1, 0, 1, 2, -1, -4]),[],res)
for i in range(10):
	print(res)
