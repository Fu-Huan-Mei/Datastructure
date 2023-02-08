
#1、创建一个调整函数:top = low,last = high（关键点：分清楚元素序号和元素的值）
 def sift(li,top,last):
# 	#2、li:表示传入的列表；top：堆顶位置（根节点的位置）；last：堆的最后一个元素的位置
# 	#3、i最开始指向根节点（堆顶）:父亲的位置
 	i = top
# 	#4、j最开始是左孩子（左子节点）：孩子的位置
 	j = 2 * i + 1
# 	#5、先找一个变量把li[top]值存起来,把堆顶的值存起来
 	variable = li[top]
# 	#6、只要j位置有数（结点），就一直循环（？）
 	while j <= last:
# 		#7、比较左孩子和右孩子的大小：如果右孩子:li[j+1]>左孩子：li[j]且有右孩子，则j指向右孩子（较大的数）
 		if j+1 <= last and li[j+1] > li[j]:
# 			#8、j指向右孩子
 			j = j + 1
 		if li[j] > variable:
			li[i] = li[j]
# 			#9、往下看一层
 			i = j
 			j = 2 * i + 1
 		else:#10、varible更大，把varible放到某一个父节点位置上的位置上
 			li[i] = variable
 			break
 	else:# 11、把varibla放到子节点位置上
 		li[i] = variable
#2、堆排序(最不好写代码):找到最后一个非叶子结点开始排序
def heap_sort(li):
	n = len(li)
	#1、从子结点找父结点公式：(i-1)//2,i=n-1,2个公式联立可以求得：（n-2)//2，每个父结点之间相差距离1
	#i的结果是：4、3、2、1、0（我自己用li1运行的结果）
	for i in range((n-2)//2,-1,-1):
		#2、i表示建堆时调整的部分的根结点的下标
	 	sift(li,i,n-1)
	# #3、建堆已完成，堆顶已是最大值
	 print(li)
	#4、挨个出数:i指向当前堆的最后一个元素，所以循环i次，即遍历列表的0~最后一个元素的次数
	 for i in range(n-1,-1,-1):
	 	li[0],li[i] = li[i],li[0]
	 	#5、i - 1是新的last,0是top
	 	sift(li,0,i-1)
#li1 = [6,8,1,9,3,0,7,2,4,5]
li = [i for i in range(10)]
import random
random.shuffle(li)
print(li)

heap_sort(li)
print(li)







