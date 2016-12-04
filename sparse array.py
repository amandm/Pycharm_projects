n = int(input())

nl = []
for i in range(n):
    t1 = input()
    nl.append(t1)

q = int(input())

ql = []
for i in range(q):
    t2 = input()
    ql.append(t2)

print(nl)
print(ql)

for k in ql:
    t = nl.count(k)
    print(t)
