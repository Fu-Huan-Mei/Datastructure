#创建双链表
class Node(object):
	def __init__(self,item=None):
		self.item = item
		self.next = None
		self.prior = None
