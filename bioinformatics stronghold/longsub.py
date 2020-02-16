# -*- coding: utf-8 -*- 



def longsub(d):
	L = [[] for i in range(len(d))]
	L[0] = [d[0],]
	for i in range(1,len(d)):
		# print L[i],
		for j in range(0,i):
			if (d[j] < d[i] and len(L[i]) < len(L[j]) + 1):
				L[i] = L[j]
			# print L[i]

		L[i] = L[i] +  [d[i],]
		print L[i]
	length = [len(i) for i in L]
	p = length.index(max(length))
	print L[p]
longsub([3,2,6,4,5,1])