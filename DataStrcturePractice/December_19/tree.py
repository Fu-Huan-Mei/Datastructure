# n = Node('hello')
# n2 = Node('world')
#从孩子节点找父节点：n.children.append(n2)
#从父节点找孩子节点：n2.parent = n
#链式存储
class Node:
	def __init__(self,name,type='dir'):
		self.name = name
		self.type = 'dir'#'dir'表示文件夹
		self.children = []
		self.parent = None
	def __repr__(self):
		return self.name
		
class FileSystemTree:
	def __init__(self):
		self.root = Node('/')#/abc.txt
		self.now = self.root

	#当前目录下创建文件夹
	def mkdir(self,name):#name是一个文件夹，以/结尾
		if name[-1] != '/':
			name += '/'
		node = Node(name)
		#正连上
		self.now.children.append(node)
		#反连接
		node.parent = self.now

	#展示当前目录下的所有内容
	def ls(self):
		return self.now.children

	#切换目录:只支持相对路径
	def cd(self,name):
		#支持向下查找
		if name[-1] != '/':
			name += '/'
		#支持向上查找目录
		if name == '../':
			self.now = self.now.parent
			return 

		for child in self.now.children:
			if child.name == name:
				self.now = child
				return
		raise ValueError('invalid dir')

#实现当前目录下创建文件夹该功能
# tree = FileSystemTree()
# tree.mkdir('var/')
# print(tree.root.children)

#展示当前目录下的所有内容
tree = FileSystemTree()
tree.mkdir('var/')
tree.mkdir('bin/')
tree.mkdir('urs/')
tree.cd('bin/')
tree.mkdir('python/')
tree.cd('../')
print(tree.ls())





