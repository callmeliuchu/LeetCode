import numpy as np

s = "ab"
t = "ahbgdc"

def isSubsequence(sub_str, mother_str):
	sub_len = len(sub_str)
	mother_len = len(mother_str)
	graph = []
	for i in range(sub_len+1):
		graph.append([0]*(mother_len+1))
	for i in range(1,sub_len+1):
		for j in range(1,mother_len+1):
			if sub_str[i-1] == mother_str[j-1]:
				graph[i][j] = graph[i-1][j-1]+1
			else:
				graph[i][j] = max(graph[i-1][j],graph[i][j-1])
	return graph[-1][-1] == sub_len

res = isSubsequence(s,t)
print(res)

