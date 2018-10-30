# 1. Basic - Print all the numbers/integers from 0 to 150
# version 1 - PREFERRED
i = 0
while i <= 150:
  print(i)
  # i += 1 is the same as i = i + 1
  # the variable named i (on the left) is being overwritten by: the value of i, plus 1
  i += 1

# version 2
# range(151) creates a list of ints from 0 - 150
# i.e. [0, 1, 2, 3, ... 148, 149, 150]
# this is not as memory efficient, so the while loop is preferred
for i in range(151):
  print(i)

# version 3
# use start and end values
for i in range(0, 151):
  print(i)

# version 4
# use start, end, and iterator
for i in range(0, 151, 1):
  print(i)

# 2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000,000
# version 1 - PREFERRED
i = 5
while i <= 1000000:
  print(i)
  i += 5

# version 2
# this version is checking whether the number is divisible by 5
# this is an unnecessary check given the constraints
# this loop will run its block many more times than the loop above
i = 5
while i <= 1000000:
  # if the remainder of i / 5 is 0: (divisible by 5)
  if i % 5 == 0:
    print(i)
  i += 1

# version 3
# range will create a list that increments by 5 - not memory efficient
for i in range(5, 1000000, 5):
  print(i)

# 3. Counting, the Dojo Way - Print integers 1 to 100.
# If divisible by 5, print "Coding" instead. If by 10, also print "Dojo"
# version 1 - PREFERRED
i = 1
while i <= 100:
  # we don't want to print multiples of 5, so we need to check first
  if i % 5 == 0:
    print("Coding")
    # there is no constraint to put this on the same line in the console
    # we only need to check this when i is divisible by 5 so we can nest it
    if i % 10 == 0:
      print("Dojo")
  else:
    print(i)
  i += 1

# version 2
for i in range(1, 101):
  if i % 5 == 0:
    print("Coding")
    if i % 10 == 0:
      print("Dojo")
  else:
    print(i)

# 4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000
# and print the final sum
# version 1 - PREFERRED
# sum is a reserved word in python, must use a different variable name
total_sum = 0
i = 1
while i <= 499999:
  # the variable named total_sum is being overwritten by the value of total sum plus i
  total_sum = total_sum + i
  # there is no constraint to check whether the number is odd
    # we know the start and end values, and how to get to consecutive odd numbers
  # counting by 2 will lead to fewer iterations through the loop and is therefore more efficient
  i += 2
print(total_sum)

# version 2
total_sum = 0
for i in range(1, 500000, 2):
  total_sum += i
print(total_sum)

# version 3
total_sum = 0
i = 0
while i <= 500000:
  if i % 2 == 0:
    total_sum += i
  i += 1
print(total_sum)

# 5. Countdown by Fours - Print positive integers starting at 2018, counting down by fours (excluding 0)
# version 1 - PREFERRED
i = 2018
while i > 0:
  print(i)
  i -= 4

# version 2
for i in range(2018, 0, -4):
  print(i)

# 6. Flexible Countdown - given low_num, high_num, mult
# print multiples of mult from low_num to high_num, using a FOR loop.
# For (2,9,3), print 3 6 9 (on successive lines)
# version 1 - PREFERRED
# since the constraints require a for loop, this is the preferred method
# a while loop example can be found below
def flexible_countdown(low_num, high_num, mult):
  # high_num in the example is INCLUSIVE, range is EXCLUSIVE, so add 1
  # increment by 1
  for i in range(low_num, high_num + 1, 1):
    # if i is divisible by mult:
      # if the remainder of i / mult is 0 (it is divisible by mult)
    if i % mult == 0:
      print(i)

flexible_countdown(2, 9, 3)

# version 2 - while loop example
def flexible_countdown(low_num, high_num, mult):
  i = low_num
  while i <= high_num:
    if i % mult == 0:
      print(i)
    i += 1

flexible_countdown(2, 9, 3)

# version 3
def flexible_countdown(low_num, high_num, mult):
  # i is not necessary, because low_num is a number that we can modify at will
  # this may make things unreadable or confusing, but this is technically possible
  while low_num <= high_num:
    if low_num % mult == 0:
      print(low_num)
    low_num += 1

flexible_countdown(2, 9, 3)

# Predict the output
# 1.
  # 3
  # 5
  # 1
  # 2

# 2.
  # TypeError
  # Range requires integers because it creates a list of integers that can be iterated through. list is not an integer, therefore range will not work.

# 3.
  # 0
  # 1
  # 2
  # 3