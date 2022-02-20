import collections;

n=int(input())
d= collections.OrderedDict()

for i in range(n):
        Word=input()
        if Word in d:
            d[Word] +=1
        else:
            d[Word] = 1

print(len(d))

for k,v in d.items():
    print(v,end=" ")