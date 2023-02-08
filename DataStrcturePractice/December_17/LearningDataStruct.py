'''
2022-12-17？？
1、
'''
#代码运行也是错误的？？？？
#栈和队列的应用：迷宫问题,元素以元组方式存储???一窍不通
#maze没有写完
from collections import deque
maze = [
	[1,1,1,1,1,1,1,1,1,1],
	[1,0,0,1,0,0,0,1,0,1],
	[1,0,0,1,0,0,0,1,0,1],
	[1,0,0,0,0,1,1,0,0,1],
	[1,0,1,1,1,0,0,0,0,1],
	[1,0,0,0,1,0,0,0,0,1],
	[1,0,1,0,0,0,1,0,0,1],
	[1,0,1,1,1,0,1,1,0,1],
	[1,1,0,0,0,0,0,0,0,1],
	[1,1,1,1,1,1,1,1,1,1]
]
dirs = [
	lambda x,y:(x+1,y),
	lambda x,y:(x-1,y),
	lambda x,y:(x,y-1),
	lambda x,y:(x,y+1),
]
# def maze_path(x1,y1,x2,y2):
# 	stack = []
# 	stack.append((x1,y1))
# 	#栈不空
# 	while(len(stack) > 0):
# 		#当前节点(x,y)??在哪里？？
# 		curNode = stack[-1]
# 		if curNode[0] == x2 and curNode[1] == y2:
# 			#走到终点
# 			for p in stack:
# 				print(p)
# 			return True
# 		#x y四个方向：上(x-1,y) 下(x+1,y) 左(x,y-1) 右(x,y+1)??
# 		for dir in dirs:
# 			nextNode = dir(curNode[0],curNode[1])
# 			#如果下一个节点能走
# 			if maze[nextNode[0]][nextNode[1]] == 0:
# 				stack.append(nextNode)
# 				maze[nextNode[0]][nextNode[1]] = 2#2表示已经走过
# 				break
# 		else:
# 			maze[nextNode[0]][nextNode[1]] = 2#2表示已经走过
# 			stack.pop()
# 	else:
# 		print('没有路可以走！')
# 		return False
# maze_path(1,1,8,8)

#使用队列解决迷宫问题
def print_r(path):
	curNode = path[-1]
	curNode = path[-1]
	while curNode[2] == -1:
		realpath.append(curNode[0:2])
		curNode = path[curNode[2]]
		#起点
	realpath.append(curNode[0:2])
	realpath.reverse()
	for node in realpath:
		print(node)
def maze_path_queue(x1,y1,x2,y2):
	queue = deque()
	queue.append(x1,y1,-1)
	path = []
	while len(queue) > 0:
		curNode = queue.pop()
		path.append(curNode)
		if curNode[0] == x2 and curNode[1] == y2:
			#终点
			print_r(path)
		#四个方向都可走
		for dir in dirs:
			nextNode  = dir(curNode[0],curNode[1])
			if maze[nextNode[0]][nextNode[1]] == 0:
				#后续节点进队，记录哪个节点带来它的
				queue.appednd((nextNode[0],nextNode[1],len(path)-1))
				maze[nextNode[0]][nextNode[1]] = 2#标记为已经走过
	else:
		print('没有路')
		return False

maze_path_queue(1,1,8,8)