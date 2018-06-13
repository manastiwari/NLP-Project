from itertools import chain
from pyspark import SparkContext
from collections import defaultdict
from pyspark.accumulators import AccumulatorParam
import spacy
import pandas as pd
import time
import multiprocessing as mp
import json




df = pd.read_csv('data.csv')
saved_column = df.TestDescription
nlp = spacy.load('en_core_web_sm')
sc = SparkContext("spark://arv-WSG37555W7-0525:7077","App")
dic = defaultdict(list)
dic[0].append([1,1])
# class ListParam(AccumulatorParam):
#     def zero(self,value):
# 	    print("value")
# 	    print(value)
#             return dic
#     def addInPlace(self,val1,val2):
	    
# 	    for k,v in val2.iteritems():
# 		val1[k].append(v)
# 	    return val1

#dict1 = sc.accumulator(dic,ListParam())

rdd = sc.parallelize(saved_column)
rdd2 = (rdd.cartesian(rdd))
tmp2 = rdd2.map(lambda x: (round(((nlp(str(x[0]).decode('utf-8'),disable=['parser','tagger','textcat']).similarity(nlp(str(x[1]).decode('utf-8'),disable=['parser','tagger','textcat']))*100))),x))
#tmp = rdd2.map(lambda x: (abs(x[1]-x[0]),x))
var = tmp2.groupByKey().map(lambda x:(x[0],list(x[1]))).collect()
f = open("output2.txt","w+")
f2 = open("output3.txt","w+")

for item in var:
	f2.write("%s\n\n" % item)
for k,v in var:
	print("\n\n")
	print(k,v)
f.write(str(var))	
f.close()	
def l(x):
	print(x)
def g(x):
	print ("\n\n\n\n\n\n\n\n")
	for k in x:
		print(k)


#def f(x1):
#	global dict1
#	val2 = defaultdict(list)
#	val2[abs(x1[0]-x1[1])].append(x1)
#	dict1+=val2

#for k in var:
#	print(k)


#print(type(dict1.value))
#di = dict1.value
#for k,v in di.iteritems():
#	print(k,v)
#	print("\n\n")
#for i in dict1.value:
#	print(i)
#	print("\n\n\n")
#print (dict1.value)

