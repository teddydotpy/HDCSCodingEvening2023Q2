#!/usr/bin/env python3
import sys

def dec_to_hex(value: int) -> str:
    # This is the basic algoritm that translates all the decimal values to hex.
    return f'{int(value/16)}{(value%16)/16}' 


def rgb_to_hex(red: int, green: int, blue: int) -> str:
    # This is the basic algoritm that translates all the rgb colors to their hex color counterparts.
    return f'#{dec_to_hex(red)}{dec_to_hex(green)}{dec_to_hex(blue)}'

def rgb_to_cmyk(red: int, green: int, blue: int) -> str:
    pass

if __name__ == "__main__":
    if len(sys.argv) == 4:
        try:
            r, g, b = map(int, sys.argv[1:])
            if all(0 <= x <= 255 for x in [r, g, b]):
                hex_color = rgb_to_hex(r, g, b)
                print(f'The HEX color is {hex_color}')
            else:
                print('RGB values must be between 0 and 255.')
        except ValueError:
            print('Invalid input. Please enter integers for RGB values.')
    else:
        print('Usage: main.py <red> <green> <blue>')
