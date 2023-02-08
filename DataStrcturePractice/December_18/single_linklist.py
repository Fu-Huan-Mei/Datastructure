'''
2022-12-18

'''
class Node:
	def __init__(self,item):
		#数据域item
		self.item = item
		#指针节点
		self.next = None

# a = Node(1)
# b = Node(2)
# c = Node(3)
# a.next = b
# b.next = c
# print(a.next.next.item)

#创建链表：头插法
# def create_linklist(li):
# 	#头节点
# 	head = Node(li[0])
# 	for element in li[1:]:
# 		#新建节点
# 		node = Node(element)
# 		node.next = head
# 		head = node
# 	return head
# def print_linklist(lk):
# 	while lk:
# 		print(lk.item,end=',')
# 		lk = lk.next
# lk = create_linklist([1,2,3])
# print_linklist(lk)

#创建链表：尾插法
def create_linklist_tail(li):
	head = Node(li[0])
	tail = head
	for element in li[1:]:
		node = Node(element)
		tail.next = node 
		tail = node
	return head
def print_linklist(lk):
	while lk:
		print(lk.item,end=',')
		lk = lk.next
lk = create_linklist_tail([1,2,3,6,8])
print_linklist(lk)