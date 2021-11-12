def my_generator():
    print("Inside my generator")
    yield 'a'
    print('ssfdfd')
    yield 'b'
    print(10+5)
    print('asdnckds')
    yield 'c'

print(my_generator())
print('print with list')
print(list(my_generator()))

print('print with for')
for char in my_generator():
  print(char)

def counter_generator(low, high):
    while low <= high:
       yield low
       low += 1

for i in counter_generator(5,10):
  print(i, end=' ')

"""
1,h --> yield low
5 10 --> 5
6 10 --> 6
7 10 --> 7
8 10 --> 8
9 10 --> 9
10 10 --> 10
"""

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

# for i in infinite_sequence():
#   print(i, end=" ")

def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

x = simpleGeneratorFun()

print(next(x))
print(next(x))
print(next(x))

def counter_generator(low, high):
    while low <= high:
       yield low
       low += 1

object_gen = counter_generator(5,10)
print(next(object_gen))
print(next(object_gen))
print(next(object_gen))

def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def weather_talk(name):
    return f"The weather is nice, {name}."

def greet_bob(greeter_func):
    return greeter_func("Bob")

print(greet_bob(say_hello))
print(greet_bob(be_awesome))
print(greet_bob(weather_talk))

def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    # second_child()
    # first_child()
    return first_child()

parent()

def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child

# print(str(parent(1)))

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)
say_whee()

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

# template
# import functools

# def decorator(func):
#     @functools.wraps(func)
#     def wrapper_decorator(*args, **kwargs):
#         # Do something before
#         value = func(*args, **kwargs)
#         # Do something after
#         return value
#     return wrapper_decorator
# decorator(say_whee)

import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

waste_some_time(999)