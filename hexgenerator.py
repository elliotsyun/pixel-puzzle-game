import random

TOP = 0xFFFFFF
BOTTOM = 0


def generate_hex_value():
    '''Generates hex values randomly'''

    color = "%06x" % random.randint(BOTTOM, TOP)
    print("This is the color: ", color)

    return color


def generate_next_value():
    '''Generates the next hex value to compare it with'''

    # bottom and top should be multiples away from the other one
    other_color = generate_hex_value()