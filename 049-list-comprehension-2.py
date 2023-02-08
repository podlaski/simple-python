numbers = ['+48757757757','+49545545545','+48700700700','+49676676676','+48920920920']

# pl_numbers = []
# for number in numbers:
#     if number[0:3] == '+48':
#         pl_numbers.append(number)

# list comprehension
pl_numbers = [number for number in numbers if number[0:3] == '+48' ]

print(f'Polish numbers = {pl_numbers}')
