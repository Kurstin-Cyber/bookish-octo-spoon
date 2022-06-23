def do_math(*args, **kwargs):
    if kwargs['operation'] == 'add':
        my_sum = 0
        for element in args:
            my_sum += element

        return my_sum

    elif kwargs['operation'] == 'multiply':
        my_product = 1
        for element in args:
            my_product *= element

        return my_product


print(do_math(10, 20, 16, 45, 8, operation="add"))
print(do_math(3, 7, 8, 2, 11, 16, operation="multiply"))


def do_math(num1, num2, *args, **kwargs):
    if 'operation' in kwargs:
        if kwargs['operation'] == 'add':
            my_sum = 0
            my_sum += num1
            my_sum += num2
            for element in args:
                my_sum += element
            return my_sum

        elif kwargs['operation'] == 'multiply':
            my_product = 1
            my_product *= num1
            my_product *= num2
            for element in args:
                my_product *= element
            return my_product


print(do_math(10, 20, 16, 54, 18, operation='add'))
print(do_math(7, 8, 4, 6, 3, 9, operation='multiply'))
