#2022-11-25
#方式一：先放入桶，再排序
#方式二：边放边排序
#1、n表示默认分的桶,数的最大范围：100
def bucket_sort(li,n=10,max_num=100):
	#2、创建buckets:桶
	#_：指代临时变量，buckets = []固有格式
	buckets = [[] for _ in range(n)]#运行结果：[[], [], [], [], [], [], [], [], [], []]
	#3、遍历列表li
	for val in li:
		#4、如何放val：一个桶放：max_num // n=10个数;i表示val放到几号桶里
		#4、问题：当max_num=100时，最大桶即10号桶的序号范围是：90~99，那100会越界，不知道放到哪个桶里
		#i = var // (max_num // n)(不要了)
#4、解决问题：桶号是从0~9,共10个桶,选择取一个小的桶号，即使是100//10=10，但n-1=10-1=9，也会自动放到9号桶里
		i = min(val // (max_num // n),n-1)
		#5、选择把val放到该去的几号桶里了，i表示桶号，val表示li的值
		buckets[i].append(val)
		#6、保持桶内顺序：从桶的最后一个元素开始遍历，j表示桶中元素的序号
		for j in range(len(buckets[i])-1,0,-1):
			#7、如果前一个数>后一个数，则交换两个位置的值
			if buckets[i][j] < buckets[i][j-1]:
				buckets[i][j],buckets[i][j-1] = buckets[i][j-1],buckets[i][j]
			#8、如果前一个数<后一个数，则已经有序，无需交换二者的位置
			else:
				break
	#9、所有元素都被放到桶里，且桶里的数据有序
	#10、再把桶里的数据挨个输出即可
	sorted_li = []
	for buc in buckets:
		sorted_li.extend(buc)
	return sorted_li

import random
li = [random.randint(0,50) for i in range(100)]
print(li)
print('*'*80)
li = bucket_sort(li)
print(li)

