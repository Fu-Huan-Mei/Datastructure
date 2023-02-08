#桶排序
#粪桶：n=100表示100个桶、
#数的最大范围：max_num表示
def bucket_sort(li,n=10,max_num=100):
	#创建n个桶（列表）
	buckets = [[] for _ in range(n)]
	#遍历列表中的数值（找对象）
	for val in li:
		#一个桶里放（max_num//n)个数
		#i表示把val放到几号桶里(难点)
		i =min((val // (max_num // n),n-1)
		#把数值放到相对应的桶里
		buckets[i].append(val)
		#保持桶内有序,倒序遍历
		for j in range(len(buckets[i])-1,0,-1):
			if buckets[i][j] < buckets[i][j-1]:
				buckets[i][j],buckets[i][j-1] = buckets[i][j-1],buckets[i][j]
			else:
				break
	#把桶里的数字输出即可
	sorted_li = []
	for buc in buckets:
		sorted_li.extend(buc)
	return sorted_li

import random 
li = [random,randint(0,10) for i in range(100)]		
print(li)
li = bucket_sort(li)
