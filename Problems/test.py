class ListNode:
	def __init__(self,x):
		self.val = x
		self.next = None


def createLink(arr):
	if len(arr) == 0:
		return None
	head = ListNode(arr[0])
	p = head
	for i in range(1,len(arr)):
		q = ListNode(arr[i])
		p.next = q
		p = q
	return head

def visitLink(head):
	p = head
	while p:
		print(p.val)
		p = p.next


def getArr(head):
	p = head
	res = []
	while p:
		res.append(p.val)
	return res

def reverse(arr,start,end):
	mid = (start + end)//2
	for i in range(start,mid+1):
		other = start + end - i
		print(i,other)
		tmp = arr[i]
		arr[i] = arr[other]
		arr[other] = tmp


def reverseByK(arr,k):
	slice_num = len(arr) // k
	for i in range(1,slice_num+1):
		reverse(arr,i*k-k,i*k-1)




arr = [1,2,3,4,5,5,6,7]
head = createLink(arr)
reverseByK
# head = createLink(arr)
# visitLink(head)






