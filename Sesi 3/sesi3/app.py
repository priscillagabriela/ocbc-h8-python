# required arg (positional order) non-keyword
# keyword argument
# default argument
# variable length-nonkeyword
# variable length-keyword

def save_personal_info(name,age):
    print('name:', name)
    print('age:', age)
    pass

# required
save_personal_info('ani',22)
save_personal_info('adi',37)


# keyword
save_personal_info(name='lucy',age=17)
save_personal_info(age=17,name='lucy') #out of order

# default
def save_personal_info(name,age=18):
    print('name:', name)
    print('age:', age)
    pass

name='Ria'
save_personal_info('Ria')

# eggs,wheat,flour,chocolate bar, etc
# roy buy 1 item:chocolate bar
# tia buy 4 item:eggs,wheat,flour,chocolate bar

def buy(customer_name,*items):
    # print etc etc
    pass

buy('roy','chocolate')
buy('tia','eggs','wheat','flour','chocolate bar')

# practice
def my_function(p, l):
    '''Function to calculate area of a square'''
    print(p * l)

# def printme( str_input ):
#    '''This prints a passed string into this function'''
#    print(str_input)

my_function(11,15)
# printme('this is me trying')

def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)

printme("I'm first call to user defined function!")
printme("Again second call to the same function")

def print_boolean( answer ):
   '''This prints a passed string into this function'''
   print('\nThe answer is',answer)

print_boolean(True)

def calculate_rect(length, width):
  '''This function is used to calculate area of rectangle'''
  print('Area : ', length*width)

length = 100
width = 20

calculate_rect(width,length)

def buy(customer_name,address,*items):
    print(customer_name)
    print(items)
    # print etc etc
    pass

buy('roy','chocolate')
buy('tia','eggs','wheat','flour','chocolate bar')

# kalo 1 bintang tuple
# klo 2 bintang dictionary

# .items() 
#                     key=    value=
#     1st iteration: jimmy,'chevrolet',       for key, value in dict_name.items()
#     2nd iteration: frank,'ford',
#     3rd iteration: tine,'honda'
# .keys()
#                     key=    
#     1st iteration: jimmy,                   for key in dict_name.keys()
#     2nd iteration: frank,
#     3rd iteration: tine,
# .values()
#                    value=
#     1st iteration: 'chevrolet',             for value in dict_name.values()
#     2nd iteration: 'ford',
#     3rd iteration: 'honda'

# lambda
def sum(num1,num2):
    return num1+num2

hasil = lambda num1,num2: num1 + num2

calculated_rect_area = lambda length,width: length*width

total = 0

def sum( arg1, arg2 ):
   total = arg1 + arg2; 
   print("Inside the function local total   : ", total)

sum( 10, 20 )
print("Outside the function global total : ", total)

total = 0

def sum( arg1, arg2 ):
   total = arg1 + arg2; 
   print("Inside the function local total   : ", total)
   return total

print("Outside the function global total - before : ", total)
total = sum( 10, 20 )
print("Outside the function global total - after  : ", total)

# module and package
import person

# external reference
def my_function(p, l):
    '''Function to calculate area of a square'''
    print(p * l)


def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)

printme("I'm first call to user defined function!")
printme("Again second call to the same function")

def changeme( mylist ):
   '''This changes a passed list into this function'''
   mylist = mylist+[1,2,3,4]
   print("\nValues inside the function : ", mylist)
   return mylist

mylist = [10,20,30]
print("\nValues outside the function - before : ", mylist)
mylist = changeme( mylist )
print("\nValues outside the function - after  : ", mylist)

def changeme( mylist ):
   '''This changes a passed list into this function'''
   mylist = [1, 2, 3, 4]
   print("Values inside the function  : ", mylist)

mylist = [10, 20, 30]
changeme( mylist )
print("Values outside the function : ", mylist)

def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)
 
printme("Hello")

def calculate_rect(length, width):
  '''This function is used to calculate area of rectangle'''
  print('Area : ', length*width)

length = 100
width = 20

calculate_rect(length, width)

def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)

printme(str_input = "Hacktiv8")

def printinfo( name, age ):
   '''This prints a passed info into this function'''
   print("Name : ", name)
   print("Age. : ", age)

printinfo( age=4, name="a" )

def printinfo( name, age = 26 ):
   '''This prints a passed info into this function'''
   print("Name : ", name)
   print("Age  : ", age)
   print("")

printinfo( age=50, name="hacktiv8" )
printinfo( name="hacktiv" )

def printinfo( name, age = 26 ):
   '''This prints a passed info into this function'''
   print("Name : ", name)
   print("Age  : ", age)
   print("")

printinfo( age=50, name="hacktiv8" )

def printinfo( arg1, *vartuple ):
   '''This prints a variable passed arguments'''
   print('arg1     : ', arg1)
   print('vartuple : ', vartuple)
   print('')
   
   for var in vartuple:
      print('isi vartuple : ', var) 

printinfo( 10 )
printinfo( 70, 60, 50, "a" )

def person_car(total_data, **kwargs):
  '''Create a function to print who owns what car'''
  print('Total Data : ', total_data)
  for key, value in kwargs.items():
    print('Person : ', key)
    print('Car    : ', value)
    print('')

person_car(3, jimmy='chevrolet', frank='ford', tina='honda')
person_car(3)

total = 0

def sum( arg1, arg2 ):
   total = arg1 + arg2; 
   print("Inside the function local total   : ", total)
   return total

print("Outside the function global total - before : ", total)
total = sum( 10, 20 )
print("Outside the function global total - after  : ", total)

def sum_number(num1, num2):
  '''
  This function is used to sum of 2 variables.
  :param num1: Input number 1 | int or float
  :param num2: Input number 2 | int or float
  
  :return: num3: Sum of number | int or float
  '''

  num3 = num1 + num2
  return num3
  
print(sum_number.__doc__)