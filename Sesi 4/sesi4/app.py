print('File')

# OPEN
file = open('Hack8_Sample_Text.txt')

file.close()

try:
   file = open("Hack8_Sample_Text.txt")
   print('Opening the file')
finally:
   print('Closing the file')
   file.close()

# WRITE
with open("sample.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")

# READ
f = open("sample.txt",'r',encoding = 'utf-8')
data = f.read(4)
print(data)

data = f.read(4)
print(data)

data = f.read()
print(data)

# APPEND
f = open("sample.txt",'a',encoding = 'utf-8')

data = f.write('\n404\n')
print(data)

with open("sample.txt",'r',encoding = 'utf-8') as f:
   data = f.read(4)
   print(data)
   data = f.read(4)
   print(data)

   n = f.tell()
   print(n)

   data = f.read(12)
   print(data)
   n = f.tell()
   print(n)

   f.seek(15)
   data = f.read(3)
   print(data)

   f.seek(0)
   for line in f:
       print(line, end = ' ')

   f.seek(0)
   data = f.readline()
   print(data)
   data = f.readline()
   print(data)
   data = f.readline()
   print(data)
   data = f.readline()
   print(data)
   data = f.readline()
   print(data)

   f.seek(0)
   data = f.read()
   print(data)

# EXCEPTION
x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

# ASSERTION
import sys
print(sys.platform)
assert ('linux' in sys.platform), "This code runs on Linux only."
assert ('win32' in sys.platform), "This code runs on Windows only."

# HANDLING EXCEPTION
coins = 10
def check_coins(coins):
    assert(coins > 10), "some coins fell down on the way"

coins = 8
try:
    check_coins(coins)
except:
    raise Exception('some message coins fell here--')

import sys
def os_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    assert ('win32' in sys.platform), "This code runs on Windows only."
    print('Doing something.')
try:
    os_interaction()
    print('masuk ke try blok')
except:
    print('masuk ke except blok')
    print('Linux function was not executed')
    pass

import sys
def os_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    assert ('win32' in sys.platform), "This code runs on Windows only."
    print('Doing something.')
try:
    os_interaction()
except AssertionError as error:
    print(error)
    print('The os_interaction() function was not executed')

try:
    with open('file.log') as file:
        read_data = file.read()
except:
    print('Could not open file.log')
print(100200)

try:
    # with open('file.log') as file:
    with open('sample.txt') as file:
        read_data = file.read()
    # with open('file.log') as file:
    #     read_data = file.read()
    n=10
    print(n)
except FileNotFoundError as error:
    print(error)
    print('%#')
else:
    print('Executing the else clause')
    print('harus ditampilkan')

import sys
def os_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    assert ('win32' in sys.platform), "This code runs on Windows only."
    print('Doing something.')
try:
    os_interaction()
except AssertionError as error:
    print(error)
else:
    print('Executing the else clause')
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    finally:
        print('Cleaning up, irrespective of any exceptions.')

try:
    with open('file.log') as file:
        read_data = file.read()
except:
    print('Could not open file.log')
print(100200)