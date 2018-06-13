from itertools import chain
from pyspark import SparkContext
from collections import defaultdict
from pyspark.accumulators import AccumulatorParam
sc = SparkContext("spark://project-VirtualBox:7077","App")
dic = defaultdict(list)
dic[0].append([1,1])
class ListParam(AccumulatorParam):
    def zero(self,value):
	    print("value")
	    print(value)
            return dic
    def addInPlace(self,val1,val2):
	    
	    for k,v in val2.iteritems():
		val1[k].append(v)
	    return val1

dict1 = sc.accumulator(dic,ListParam())

rdd = sc.parallelize(range(1,2000))
rdd2 = (rdd.cartesian(rdd))
tmp = rdd2.map(lambda x: (abs(x[1]-x[0]),x))
var = tmp.groupByKey().map(lambda x:(x[0],list(x[1]))).collect()
print(var)
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
	
