'''
2022-12-16
1、练习题
2、数据结构

'''

#队列：刚开始创建时要指定长度
# class Queue:
# 	def __init__(self,size=100):
# 		self.queue = [0 for _ in range(size)]
# 		self.size = size
# 		self.rear = 0#队尾指针
# 		self.front = 0#队首指针
# 		#进队（入队）
# 	def push(self,element):
# 		if not self.is_fulled():
# 			#队尾指针后移一个并插入新值
# 			self.rear = (self.rear+1) % self.size
# 			self.queue[self.rear] = element
# 		else:
# 			raise IndexEorror('队列已满！')
# 		#出队
# 	def pop(self):
# 		if not self.is_empty():
# 		#队首指针后移一个
# 			self.front = (self.front + 1) % self.size
# 			return self.queue[self.front]
# 		else:
# 			raise IndexEorror('队列是空的!')
# 		#判断队空
# 	def is_empty(self):		
# 		return self.rear == self.front
# 		#判断队满
# 	def is_fulled(self):
# 		return (self.rear + 1) % self.size == self.front
# q = Queue()
# for i in range(4):
# 	q.push(i)
# print(q.is_fulled())
# r = q.pop()#先进先出，显先出队列的是0
# print(r)
# q.push(4)

#使用内置模块创建队列
#这里不怎么懂？？？
#单向队列
from collections import deque
q = deque([1,2,3,4,5,6])
#队尾进队
q.append(7)
#队首出队
r  = q.popleft()
print(r)

#双向队列
q.appendleft(1)
r = q.pop()
print(r)


# #栈
# class Stack:
# 		#建立一个空列表
# 	def __init__(self):
# 		self.stack = []
# 		#进栈
# 	def push(self,element):
# 		self.stack.append(element)
# 		#出栈
# 	def pop(self):
# 		return self.stack.pop()
# 		#取栈顶
# 	def get_top(self):
# 		#判断栈有数
# 		if len(self.stack) > 0:
# 			return self.stack[-1]
# 		else:
# 			return None
# 			#判断栈是否为空
# 	def is_empty(self):
# 		return len(self.stack) == 0
# #栈的应用
# #括号匹配问题
# def brace_match(s):
# 	match = {'}':'{',')':'(',']':'['}
# 	stack = Stack()
# 	#进栈
# 	for chareter in s:
# 		if chareter in {'(','{','['}:#字典的值
# 			#进栈
# 			stack.push(chareter)
# 		else:
# 			#如果栈为空，则结束
# 			if stack.is_empty():
# 				return false
# 				#去栈顶找另一半括号即找到字典中的键:匹配就出栈
# 			elif stack.get_top() == match[chareter]:
# 				stack.pop()
# 			else:#stack.get_top() != match[chareter]:
# 				return False
# 	if stack.is_empty():#说明括号都匹配
# 		return True
# 	else:
# 		return False		
# str = list('{{{{[]}}}}')
# r = brace_match(str)
# print(r)


#第一种方法：性能低
# def twoSum(li,target):
# 	n = len(li)
# 	for i in range(n):
# 		for j in range(i+1,n):
# 			if i != j:#这点我没有想到,不要输出自己和自己
# 				if li[i] + li[j] == target:
# 					return sorted([i,j])
# li = [2,7,11,15]#i 2(0)         7(1)        11(2)      15(3)
#                 #j 7 11 15(3)   11 15(2)    15(1)      0(0)
# r = twoSum(li,9)
# print(r)

#第二种方法：提高性能，二分查找
# def binary_search(self,li,val):
# 	left = 0
# 	right = len(li) - 1
# 	while left <= right:#说明候选区有值
# 		mid = (left + right) // 2
# 		if li[mid] == val:
# 			return mid
# 		elif li[mid] > val:
# 			right = mid -1
# 		else:#li[mid] < val:
# 			left = mid + 1
# 	else:#循环结束，说明没有找到
# 		return None



