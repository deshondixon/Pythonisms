# Generator
def count_up(n):
    # while n is less than 1000
    while n < 100:
        # returns the current of n to the caller
        # produces a value but pauses the execution of the loop
        # preserves the state of n in memory
        yield n
        # increments n by 1
        n += 6


# Starts count at 0
for number in count_up(0):
    # Divides each individual number by 2
    number *= 2
    print("Generator")
    print(number)

print("--------------------------------")
# Starts count at 0
count = count_up(0)
# Stops at each individual number and divides by 2
# next returns the element in the count
print(next(count) - 2)
print(next(count) - 2)
print(next(count) - 10)
print(next(count) // 10)
print(next(count) + 30)
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))

print("--------------------------------")
