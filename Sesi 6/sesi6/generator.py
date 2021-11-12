def counter_generator(low, high):
    while low <= high:
       yield low
       low += 1

# m = 5
# n = 10
# object_gen = counter_generator(m,n)
object_gen = counter_generator(5,10)