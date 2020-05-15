a = ['a','b','c','d']


a.insert(1,'e')
a.insert(1,'f')
a.insert(1,'g')
#print(a)
print(a.index('g'))
a.remove('a')
print(a.index('g'))
print(a)
print(a.index('g'))

z = sorted(a)
x = a.sort()

print(z,'$$$')
print(x,'$$$')

lst = ['1','2','Z','a','b','c']
#lst.sort()
for i in lst:
	print(i)

print(sorted(lst))
