mi_set = set([1,2,3,4,5,6,7,8,9,10])
s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}
s3 = s1.union(s2)
print(mi_set)
print(type(mi_set))
print(2 in mi_set)
print(s3)
mi_set.discard(1)
print(mi_set)
mi_set.pop()
print(mi_set)