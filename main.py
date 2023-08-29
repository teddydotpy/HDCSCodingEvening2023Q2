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
        # This entire small section exists simply to throw an error if the inputs have a float.
        check_if_floats = lambda x: isinstance(x, float) and exec('raise ValueError()')
        map(check_if_floats, arguments)

        # This is just to make sure I am in range
        if all(0 <= x <= 255 for x in [red, green, blue]):
            hex_color = f'#{dec_to_hex(red)}{dec_to_hex(green)}{dec_to_hex(blue)}'
            return hex_color
        else:
            return 'RGB values must be between 0 and 255.'
    except ValueError:
        return 'Invalid input. Please enter integers for RGB values.'

def rgb_to_cmyk(arguments: list) -> str:
    # This is the basic algoritm that translates all the rgb colors to their hex color counterparts.
    try:
        red, green, blue = map(int, arguments[1:])
        # This entire small section exists simply to throw an error if the inputs have a float.
        check_if_floats = lambda x: isinstance(x, float) and exec('raise ValueError()')
        map(check_if_floats, arguments)

        # This is just to make sure I am in range
        if all(0 <= x <= 255 for x in [red, green, blue]):
            converted_rgb = [red/255, green/255, blue/255]
            k = 1 - max(converted_rgb)
            c = (1 - converted_rgb[0] - k) / 1 - k
            m = (1 - converted_rgb[1] - k) / 1 - k
            y = (1 - converted_rgb[2] - k) / 1 - k
            cmyk = [c, m, y, k]
            return cmyk
        else:
            return 'RGB values must be between 0 and 255.'
    except ValueError:
        return 'Invalid input. Please enter integers for RGB values.'

if __name__ == "__main__":
    if len(sys.argv) == 4:
        print(f'The HEX color is {rgb_to_hex(arguments=sys.argv)}')
    else:
        print('Usage: main.py <red> <green> <blue>')
