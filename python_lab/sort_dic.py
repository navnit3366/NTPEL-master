'''
Lab Experiment 5c: Write a python script to sort a dict by values.
'''

import operator

d={1:2,3:4,9:3,2:4,6:2}
d=dict(sorted(d.items(),key=operator.itemgetter(1)))
print("Dictionary sorted by ascending order is:",d,end="\n")
d=dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
print("Dictionary sorted by descending order is:",d,end="\n")