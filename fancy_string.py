import time
import sys
import os
from enum import Enum

"""
    animation_simple() simply prints letter after letter
"""
def animation_simple(input_string, delay_second=0.01):
    current_string = ""
    # get terminal width
    terminal_width = os.get_terminal_size().columns

    for target_char in input_string:
        if target_char == '\n':
            # Print a newline and reset current_string
            print()
            current_string = ""
            continue    
        # udpate the current_string
        current_string += target_char
        # Print the updated current string
        sys.stdout.write('\r' + current_string)
        sys.stdout.flush()
        time.sleep(delay_second)
    print()

"""
    animation_increasing() prints all the letters from the current letter from [a-zA-Z].
"""
def animation_increasing(input_string, delay_second=0.005):
    current_string = ""
    # get terminal width
    terminal_width = os.get_terminal_size().columns

    for target_char in input_string:
        if target_char == '\n':
            # Print a newline and reset current_string
            print()
            current_string = ""
            continue
        if target_char == ' ':
            current_string += target_char
            sys.stdout.write('\r' + current_string)
            sys.stdout.flush()
            continue

        current_char = 'a'
        while current_char != target_char:
            # Check if the current length is at the terminal width limit
            if len(current_string + current_char) >= terminal_width:
                print()
                current_string = ""
                
            # Print the current progress with the next character
            sys.stdout.write('\r' + current_string + current_char)
            sys.stdout.flush()
            time.sleep(delay_second)
            
            # Move to the next char (used ASCII)
            current_char = chr(ord(current_char) + 1)
            if current_char == '{':  # After 'z'
                current_char = 'A'
            elif current_char == '[':  # After 'Z'
                current_char = target_char
                
        # udpate the current_string
        current_string += target_char
        # Print the updated current string
        sys.stdout.write('\r' + current_string)
        sys.stdout.flush()
    print()

def animation_bouncing_ball(input_string, delay_second=0.1, height=5):
    length = len(input_string)
    # Ensure total iterations is a multiple of height
    total_iterations = ((length + 2 * height) // height + 1) * height
    
    for i in range(total_iterations):
        if i < length:
            current_string = input_string[:i+1]
        else:
            current_string = input_string
        
        offset = height - abs(i % (2 * height) - height)
        # Clear the line first by overwriting with spaces, then print the current string
        sys.stdout.write('\r' + ' ' * (height + length) + '\r')
        sys.stdout.write(' ' * offset + current_string)
        sys.stdout.flush()
        time.sleep(delay_second)
    
    # Ensure to clear the line completely at the end and print the original string at the original position
    sys.stdout.write('\r' + ' ' * (height + length) + '\r')
    sys.stdout.write(input_string)
    sys.stdout.flush()
    print()  # Move to the next line after finishing

def animation_display_board(input_string, delay_second=0.1, repeat=3):
    width = len(input_string) + 5
    initial_padded_string = ' ' * width + input_string + ' ' * 5
    repeated_padded_string = (' ' * 5).join([input_string] * repeat) + ' ' * width
    total_length = len(repeated_padded_string)

    for i in range(len(initial_padded_string) - width + 1):
        sys.stdout.write('\r' + initial_padded_string[i:i+width])
        sys.stdout.flush()
        time.sleep(delay_second)

    for i in range(total_length - width + 1):
        sys.stdout.write('\r' + repeated_padded_string[i:i+width])
        sys.stdout.flush()
        time.sleep(delay_second)
    sys.stdout.write('\r' + input_string)
    sys.stdout.flush()
    print()


colors = {
        "RED": '\033[91m',
        "LIGHT_RED": '\033[38;5;203m',
        "ORANGE": '\033[38;5;208m',
        "YELLOW": '\033[93m',
        "GREEN": '\033[92m',
        "LIGHT_GREEN": '\033[38;5;119m',
        "CYAN": '\033[96m',
        "LIGHT_BLUE": '\033[94m',
        "BLUE": '\033[38;5;27m',
        "PURPLE": '\033[95m',
        "MAGENTA": '\033[38;5;201m',
        "PINK": '\033[38;5;218m',
        "WHITE": '\033[97m',
        "GRAY": '\033[90m',
    }

def color_simple(input_string, color):
    terminator = "\033[0m"
    
    if color.upper() not in colors:
        raise ValueError(f"Color {color} not available. Choose from: {', '.join(colors.keys())}")
    
    initiator = colors[color.upper()]
    
    print(initiator + input_string + terminator)

def color_alternating(input_string, max_time, delay_second=0.1):
    terminator = "\033[0m"
    start_time = time.time()
    
    while (time.time() - start_time) < max_time:
        for color in colors:
            if (time.time() - start_time) >= max_time:
                break
            initiator = colors[color]
            to_print = initiator + input_string + terminator
            sys.stdout.write('\r' + to_print)
            sys.stdout.flush()
            time.sleep(delay_second)
    print('\r' + input_string)

def color_alternating_individual(input_string, max_time, delay_second=0.05):
    terminator = "\033[0m"
    start_time = time.time()
    keys = list(colors.keys())
    length = len(input_string)
    
    while (time.time() - start_time) < max_time:
        to_print = ""
        for i, char in enumerate(input_string):
            color_key = keys[(i + int((time.time() - start_time) / delay_second)) % len(colors)]
            to_print += colors[color_key] + char + terminator
        sys.stdout.write('\r' + to_print)
        sys.stdout.flush()
        time.sleep(delay_second)
    
    print('\r' + input_string)


def animation_blinking(input_string, max_time, delay_second=0.5):
    start_time = time.time()
    
    while (time.time() - start_time) < max_time:
        sys.stdout.write('\r' + input_string)
        sys.stdout.flush()
        time.sleep(delay_second)
        sys.stdout.write('\r' + ' ' * len(input_string))
        sys.stdout.flush()
        time.sleep(delay_second)
    
    print('\r' + input_string)
