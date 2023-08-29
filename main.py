#!/usr/bin/env python3
import sys

hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
def dec_to_hex(value: int) -> str:
    # This is the basic algoritm that translates all the decimal values to hex.
    return f'{hex[int(value/16)]}{hex[int(value%16)]}' 


def rgb_to_hex(arguments: list) -> str:
    # This is the basic algoritm that translates all the rgb colors to their hex color counterparts.
    try:
        red, green, blue = map(int, arguments[1:])
        check_if_floats = lambda x: isinstance(x, float) and exec('raise ValueError()')
        list(map(check_if_floats, arguments))
        if all(0 <= x <= 255 for x in [red, green, blue]):
            hex_color = f'#{dec_to_hex(red)}{dec_to_hex(green)}{dec_to_hex(blue)}'
            return hex_color
        else:
            return 'RGB values must be between 0 and 255.'
    except ValueError:
        return 'Invalid input. Please enter integers for RGB values.'

def rgb_to_cmyk(red: int, green: int, blue: int) -> str:
    pass

if __name__ == "__main__":
    if len(sys.argv) == 4:
        print(f'The HEX color is {rgb_to_hex(arguments=sys.argv)}')
    else:
        print('Usage: main.py <red> <green> <blue>')
