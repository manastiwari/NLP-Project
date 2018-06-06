from itertools import chain
from pyspark import SparkContext
from collections import defaultdict
from pyspark.accumulators import AccumulatorParam
sc = SparkContext("local","App")
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

rdd = sc.parallelize([1,2,3,4,5,6,7,8,9,10,11,12])
rdd2 = rdd.cartesian(rdd)

def f(x1):
	global dict1
	val2 = defaultdict(list)
	val2[abs(x1[0]-x1[1])].append(x1)
	dict1+=val2

rdd2.foreach(f)
print(type(dict1.value))
di = dict1.value
#for k,v in di.iteritems():
#	print(k,v)
#	print("\n\n")
#for i in dict1.value:
#	print(i)
#	print("\n\n\n")
#print (dict1.value)
	

