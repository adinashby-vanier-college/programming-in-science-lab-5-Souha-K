# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    if (n == 1):
        return ('*')
    elif (n == 2):
        return ('**\n**')
    else:
        while (n >= 3):
            #      top        '*' 1         space      '*' 2                    bottom line
            x = (('*' * n) + (('\n*' + (' ' * (n - 2)) + '*') * (n - 2)))  + ('\n' + (('*' * n)))
            return (x) 

n = int(input('Enter value: ')) 
output = hollow_square(n)
print(output)

# 1
# 12
# 123
# 1234
def number_pattern(n):
    if n == 1:
        return 1
    elif n == 2:
        return str(12)
    else: 
        while n >= 3:
            x = range(1, n, -1)
            return x
   
n = int(input('Enter value: ')) 
output = number_pattern(n)
print(output)


# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    pass
    # n = ('Enter number: ')
    # numbers = (1, 2, 3, 4, 5, 6)
    # addition = 1
    # numbers += addition
    # return n

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    pass
    # return ""

# count = '*'
# while count <= '****':
#     print(count)
#     count += '*'
