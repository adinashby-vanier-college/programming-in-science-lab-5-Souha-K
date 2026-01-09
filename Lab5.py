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

# n = int(input('Enter number: ')) 
# output = hollow_square(n)
# print(output)

# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ''
    
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            result += str(j)
        result += "\n"


    return result.rstrip()

# n = int(input('Enter number: '))
# output = number_pattern(n)
# print(output)


# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):    
    count = 0

    for i in range(1, n + 1):
        count += i
    
    return count

# n = int(input('Enter number: '))
# print(sum_of_natural_numbers(n))


# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ''
    count = '*'

    for i in range(n + 1):
        result += count

        for j in range(1, i + 1):
            result += count
            result += ' '
            result += '\n'


    return result

n = int(input('Enter number: '))
output = centered_star_pyramid(n)
print(output)
