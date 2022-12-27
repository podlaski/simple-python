# Sum of expenses

sum_ = 0
expenses = [10, 40, 50, 55, 60, 100]

for expense in expenses:
  sum_ += expense

# version 1
print('Version 1: $', sum_)

# option 2
print('Version 2: $', sum(expenses))
