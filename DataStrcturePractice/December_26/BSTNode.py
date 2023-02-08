#二叉搜索树:代码有问题？？
#树中节点的定义如下：
import random
class BiTreeNode:
	def __init__(self,data):
		self.data = data
		self.lchild = None#为什么是None????
		self.rchild = None
		self.parent = None

class BST:
	def __init__(self,li=None):
		self.root = None#根节点
		if li:
			for val in li:
				self.insert_no_rec(val)

		#插入函数:递归
		#node表示插到哪个节点，val表示要插入的值
	def insert(self,node,val):
		#node是空：if node == None与if not node:含义相同
		if not node:
			#如果是空树：重新创建node节点，直接把val插入该节点即可，？？？后面不理解：但是没有被树连起来，所以return node
			node = BiTreeNode(val)
			#如果不是空树
		elif val < node.data:
			#连接左孩子节点
			node.lchild = self.insert(node.lchild,val)
			#连接父节点
			node.lchild.parent = node
		elif val > node.data1:
			node.rchild = self.insert(node,rchild,val)
			node.rchild.parent = node
		return node

		#插入：非递归
	def insert_no_rec(self,val):
		p = self.root#???
		if not p:#空树 if p == None
			self.root = BiTreeNode(val)
			return 
		while True:#如果不是空树
			if val < p.data:#往左子树插入
				if p.lchild:#先判断左子树是否有值
					p = p.lchild
				else:#左孩子不存在
					p.lchild = BiTreeNode(val)
					p.lchild.parent = p
			elif val > p.data:
				if p.rchild:
					p = p.rchild
				else:
					p.rchild = BiTreeNode(val)
					p.rchild.parent = p
					return
			else:
				return 

	#遍历
	#前序遍历
	def pre_order(self,root):
		if root:
			print(root.data,end='')
			self.pre_order(root.lchild)
			self.pre_order(root.rchild)

	#中序遍历
	def in_order(self,root):
		if root:
			self.in_order(root.lchild)
			print(root.data,end='')
			self.in_order(root.rchild)

	#后序遍历
	def post_order(self,root):
		if root:
			self.post_order(root.lchild)
			self.post_order(root.rchild)
			print(root.data,end='')
tree = BST([4,6,7,9,2,1,3,5,8])
tree.pre_order(tree.root)
print('')
tree.in_order(tree.root)
print('')
tree.post_order(tree.root)

	#查询:递归版本
	def query(self,node,val):#此行代码有问题：unexpected indent
		if not node:
			return None
		if node.data < val:
			return self.query(node.rchild,val)
		elif node.data > val:
			return self.query(node.lchild,val)
		else:
			return node
	
	#查询：非递归版本
	def query_no_rec(self,val):
		p = self.root
		while P:#p不是空
			if p.data < val:
				p = p.rchild
			elif p.data > val:
				p = p.lchild
			else:
				return p
		return None
	 
li = list(range(0,500,2))
random.shuffle(li)
tree = BST(li)
print(tree.query_no_rec(4))

#删除：3种情况
#第一种情况：node是叶子节点
	def __remove_node_1(self,node):
		if not node.parent:
			self.root = None
		if node == node.parent.lchild:#node是父亲的左孩子节点
			node.parent.lchild = None
			node.parent  = None
		else:#node是父亲的右孩子节点
			node.parent.rchild = None
			node.parent  = None

	#第二种情况：node只有一个左孩子节点
	def __remove_node_2(self,node):
		if not node.parent:#node就是根节点
			self.root = node.lchild
			node.lchild.parent = None
		elif node == node.parent.lchild:#node为左孩子节点,下面两步完全糊涂？？
			node.parent.lchild = node.lchild
			node.lchild.parent = node.parent
		else:
			node.parent.rchild = node.lchild
			node.lchild.parent = node.parent
	#第二种情况：node只有一个右孩子节点
	def __remove_node_3(self,val):
		if not node.parent:
			self.root = node.rchild
		elif node == node.parent.lchild:
			node.parent.lchild = node.rchild
			node.rchild.parent = node.parent
		else:
			node.parent.rchild = node.rchild
			node.rchild.parent = node.parent

	#第三种情况：先找到节点，再删除节点？？？没有听懂
	def delete(self,val):
		if self.root:#不是空树
			node = self.query_no_rec(val)
			if not node:
				return False
			if not node.lchild and not node.rchild:#情况一：node是叶子节点
				self.__remove_node_1(node)
			elif not node.rchild:#只有一个左孩子
				self.__remove_node_2(node)
			elif not node.lchild:#只有一个右孩子
				self.__remove_node_3(node)
			else:#两个孩子都有
				min_node = node.rchild
				while min_node.lchild:
					min_node = min_node.lchild
				node.data = min_node.data
				# 删除min_node
				if min_node.rchild:
					self.__remove_node_3(min_node)
				else:
					self.__remove_node_1(min_node)
tree = BST([1,4,2,5,3,8,6,9,7])
tree.in_order(tree,root)
print('')
tree.delete(4)












