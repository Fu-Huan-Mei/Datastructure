'''
2022-12-26
1、AVL树
'''
import BiTreeNode,BSTNode
#插入
class AVLNode(BiTreeNode):
	def __init__(self,li=None):
		BST.__init__(self,li)

	#左旋（看图来写）
	def rotate_left(self,p,c):
		s2 = c.lchild
		p.rchild = s2
		if s2:
			s2.parent = p

		c.lchild = p
		p.parent = c

		#bf表示平衡点（balance factor)
		p.bf = 0
		c.bf = 0
		return c

	#右旋（看图写代码）
	def rotate_right(self,p,c):
		s2 = c.rchild
		p.lchild = s2
		if s2:
			s2.parent = p

		c.rchild = p
		p.parent = c

		p.bf = 0
		c.bf = 0
		return c

	def rotate_right_left(self,p,c):
		g = c.lchild

		s3 = g.rchild
		c.lchild = s3
		#反向连接回去
		if s3:
			s3.parent = c
		g.rchild = c
		c.parent = g
		
		s2 = g.lchild
		p.rchild = s2
		if s2:
			s2.parent = p
		g.lchild = p
		p.parent = g
		#更新bf




