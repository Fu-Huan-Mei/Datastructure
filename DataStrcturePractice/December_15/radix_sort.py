#专心专注 高效
#基数排序，基于多关键字排序：数字 123 012、字符串排序：abcd ab00
#时间复杂度：kn，与数的范围有关
def radix_sort(li):

	max_num = max(li)#循环次数根据最大值确定循环几次 eg:99-2次 100-3次  最大数的位数是几就做几次循环
	#it表示迭代次数
	it = 0

	#10**0=1 10**1=10 10**2=100 10**3=1000
	while 10 ** it <= max_num:#难点
		#分10个桶：0~9
		buckets = [[] for _ in range(10)]

		#把var分到几号桶主要是看正在看哪个位数
		for var in li:
			#987 当It=0时，就看个位数 987%10=7，取出十位数：987//10%10=8
			digit = (var // 10 ** it) % 10
			buckets[digit].append(var)
		#分桶完成
		li.clear()

		for buc in buckets:
			#把分通完成的数重新写回li
			li.extend(buc)

		it += 1
import random
li = list(range(100))
random.shuffle(li)
print('排序前：',li)
radix_sort(li)
print('排序后:',li)
