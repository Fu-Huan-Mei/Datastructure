#基数排序
def radix_sort(li):
	#1、根据传入数据的位数来确定最大值，即最多要循环几次：比如99两位数（2次）、190三位数（3次）
	max_num = max(li)
	#2、it迭代次数，迭代几次就循环几次
	it = 0
	while 10 ** it <= max_num:#仔细思考哦！！！（难点）
	#3、分10个桶，序号分别为：0 1 2 3 4 5 6 7 8 9
		buckets = [[] for _ in range(10)]
	#4、把每一个元素分别放到桶里
		for val in li:
		#5、这个元素放到记号桶呢？取决于当前看的哪位数：根据it来看
		#5、例子：987:it=1时取十位数：987 // 10 % 10=8;it=2时即取百位数：987//100%10
		#5、已经知道了放记号桶
			digit = (val // 10 ** it) % 10
		#6、把val进行分桶
			buckets[digit].append(val)
	#7、分桶完成？不就已经把数据放到桶里了吗？列表已经空了呀？为什么还要清空列表？？？
		li.clear()#8、清空列表
	#9、遍历桶准备排序
		for buc in buckets:
		#10、把数重新写回li，最后li已经有序了
			li.extend(buc)
		it = it + 1
	#print(it)
import random
li = list(range(100))
random.shuffle(li)
print(li)
print('*'*165)
radix_sort(li)
print(li)