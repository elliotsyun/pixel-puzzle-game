import random

TOP = 0xFFFFFF
BOTTOM = 0


def generate_hex_value():
    '''Generates hex values randomly'''

    color = "%06x" % random.randint(BOTTOM, TOP)
    print("This is the color: ", color)

    return color


def find_multiples(number, m):
    '''Prints the first m multiples of a number'''
    mul_list = []

    for i in range(0, m*number, number):
        mul_list.add(i)

    return mul_list


def generate_next_value():
    '''Generates the next hex value to compare it with'''


    # bottom and top should be multiples away from the other one
    other_color = generate_hex_value()
