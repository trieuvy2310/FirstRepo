def logical_oper():
    # Exercise: Logical Operator
    is_magician = False
    is_expert = False
    if is_magician:
        if is_expert:
            print('\nYou are the master magician')
        else:
            print("\nAt least you're getting there")
    else:
        print('You need Magic powers')


def sum_up(abc):
    # Exercise: for loop
    sum_all = 0
    for item in abc:
        sum_all += item
    print(sum_all)


sum_up(list(range(100)))
