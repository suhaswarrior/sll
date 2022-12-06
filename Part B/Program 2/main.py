from collections import Counter # Path: test.py
from functools import reduce # Path: test.py


def word_count(fname):
    with open(fname) as f:
        return Counter(f.read().split())


d = word_count("filename.txt") # Path: filename.txt
print(d)
print(type(d))
lis = list(d.items()) # convert dictionary to list
print(lis)
lis.sort(reverse=True, key=lambda x: x[1]) # sort list by value
print(lis)
print("\nThe top 10 most occured words are:")
lis2 = []
for i in range(0, 10):
    print(lis[i][0], "\n")
    lis2.append(lis[i][1])
avg = reduce(lambda a, b: a + b, lis2) / len(lis2) # find average
print("Average is :", avg) # print average
lis2 = [x * x for x in lis2 if x % 2 != 0] # find square of odd numbers
print("Final list = ", lis2)



