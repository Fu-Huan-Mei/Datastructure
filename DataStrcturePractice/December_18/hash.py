
#创建哈希函数:类似于集合的结构？？不懂
class HashTable:
	def __init__(self,size=101):
		self.size = size
		#缺少LinkList()函数
		self.T = [LinkList() for i in range(self,size)]
	def h(self,k):
		return k % self.size
	#查找i函数
	def find(self,k):
		i = self.h(k)
		return self.T[i].find(k)

		#插入
	def insert(self,k):
		i = self.h(k)
		if self.find(k):
			print("重复插入！")
		else:
			self.T[i].append(k)
ht = HashTable()
ht.insert(0)
ht.insert(1)
ht.insert(3)
ht.insert(102)
print(",".join(map(str,ht.T)))
print(ht.find(3))