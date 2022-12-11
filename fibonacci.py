x = int(input('Qual numero de fibonacci deseja saber: '))
t1 = 1
t2 = 1
if (x==1) or (x==2):
    print('1')
else:
    count = 3
    while count <= x:
        t3 = t1 + t2
        t1 = t2
        t2 = t3
        count += 1
print(t3) 