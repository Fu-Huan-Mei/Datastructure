#创建二叉树
class BiTreeNode:
	def __init__(self,data):
		self.data = data
		self.lchild = None #左孩子节点
		self.rchild = None #右孩子节点

a = BiTreeNode('A')
b = BiTreeNode('B')
c = BiTreeNode('C')
d = BiTreeNode('D')
e = BiTreeNode('E')
f = BiTreeNode('F')
g = BiTreeNode('G')

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

root = e
print(root.lchild)

#遍历二叉树：递归
#前序遍历
def pre_order(root):
	if root:
		print(root.data,end='')
		pre_order(root.lchild)
		pre_order(root.rchild)
pre_order(root)
print('*'*60)
#中序遍历
def in_order(root):
	if root:
		in_order(root.lchild)
		print(root.data,end='')
		in_order(root.rchild)
in_order(root)
print('*'*60)
#后序遍历
def post_order(root):
	if root:
		post_order(root.lchild)
		post_order(root.rchild)
		print(root.data,end='')
post_order(root)
print('*'*60)
#层次遍历（适用于多叉树）
from collections import deque

def level_order(root):
	queue = deque()
	queue.append(root)
	while len(queue) > 0:#只要队列不空
		node = queue.popleft()#出队
		print(node.data,end='')
		if node.lchild:
			queue.append(node.lchild)
		if node.rchild:
			queue.append(node.rchild)
level_order(root)
