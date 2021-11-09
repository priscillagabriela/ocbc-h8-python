x=0
y=5
if x<y:
    print('yes x < y')

if y<x:
    print('yes y < x')

if x:
    print('yes x')

if y:
    print('yes y')

if 'aul' in 'grault':
    print('yes ault in grault')

# weather = 'nice'
weather = 'cloudy'

if weather == 'nice':
    print('Mow the lawn')
    print('Weed the garder')
print('Take the dog for a walk')

if 'foo' in ['bar','baz','qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')
print('After conditional')

if 'foo' in ['foo','bar','baz']:
    print('Outer condition is true')
    if 10>20:
        print('Inner condition 1')
    print('Between inner conditions')
    if 10<20:
        print('Inner condition 2')
    print('End of outer condition')
print('After outer condition')

weather = 'cloudy'

if weather == 'nice':
    print('Mow the lawn')
    print('Weed the garder')
    print('Take the dog for a walk')
else:
    print('Read a book')
    print('Watch the movies')

hargaBuku = 20000
hargaMajalah = 5000
uang = 2000

if uang > hargaBuku:
    print("beli buku")
else:
    print("uang tidak cukup - buku")


if uang > hargaMajalah:
    print("beli buku")
else:
    print("uang tidak cukup - majalah")

hargaBuku = 20000
hargaMajalah = 5000
uang = 7000

if uang > hargaBuku:
    print("beli buku")
elif uang > hargaMajalah:
    print("beli majalah")
else:
    print("uang tidak cukup")
print("pulang")

name = 'Nindya'
if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
    print('Hello Xander')
elif name == 'Hacktiv8':
    print('Hello Hacktiv8')

hargaBuku = 20000
hargaMajalah = 5000
uang = 2000

if uang > hargaBuku: print("beli buku")
else: print("uang tidak cukup")

name = 'Nindya'
if name == 'Fred': print('Hello Fred'); print('Welcome')
elif name == 'Xander': print('Hello Xander'); print('Welcome')
elif name == 'Hacktiv8': print('Hello Hacktiv8'); print('Welcome')

if 'f' in 'foo': print('1'); print('2'); print('3')

nomor_undian = 80
if nomor_undian < 100:
    prize = 'box 1'
else:
    prize = 'box 2'

# prize = 'box 1' if nomor_undian < 100 else prize = 'box2'
print(prize)

hargaBuku = 20000
hargaMajalah = 5000
uang = 2000
if uang > hargaBuku:
    print("beli buku")
else:
    print("uang tidak cukup - buku")
print('beli buku' if uang > hargaBuku else 'uang tidak cukup - buku')

if True:
    pass
print('foo')

# definite
# indefinite

n = 5
while n > 0:
    n -= 1
    print(n)

counter=0
while counter <= 10:
    print(counter)
    if counter == 3:
        break
    counter += 1

i=0
while i<5:
    j=0
    while j<3:
        print(i,j)

        if(j==2):
            break

        print('----')

        j += 1
    i +=1
print('xxx')
print('')
i=0
while i<5:
    j=0
    while j<6:
        print(i,j)
        j += 1
        if(j==2):
            continue

        print('----')

    i +=1

n=5
while n>0:
    n-=1
    if n==2:
        break
    print(n)
print('Loop ended')

n=5
while n>0:
    n-=1
    if n==2:
        break
else:
    print('Loop done')

a = ['foo','bar']
while len(a):
    print(a.pop(0))
    b = ['bax','qux']

    while len(b):
        print('>', b.pop(0))

#  a=['foo','bar']
#  len(a)::2
#  print(a.pop(0))
#  print('foo')
#     b = ['bez'.'qux']
#     len(b) :: 2
#     print('>', b.pop(0))
#     > baz

#     b = ['qux']
#     len(b) :: 1
#     print('>', b.pop(0))
#     > baz

books = ['Book AAA', 'Book LLL', 'Book DDD','Book CCC']
for book in books:
    print(book)

    # x = range(2,8)
    x = range(0,100,20)
    for n in x:
        print(n)

        d = {'foo':1,'bar':2,'baz':1}
        for k in d:
            print(k)
            # print()
            print(d[k])
            print(d['foo'])

for k in d.values(): #[1,2,3]
    print(k)

for k, v in d.items():
    print(k,":",v)

d.items()

"""
    'foo',1,
    'bar',2,
    'baz',3
"""