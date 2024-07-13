import time
import sys
import os

"""
    simple_animation() simply prints letter after letter
"""
def simple_animation(input_string, delay_second=0.01):
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
    increasing_animation() prints all the letters from the current letter from [a-zA-Z].
"""
def increasing_animation(input_string, delay_second=0.01):
    current_string = ""
    # get terminal width
    terminal_width = os.get_terminal_size().columns

    for target_char in input_string:
        if target_char == '\n':
            # Print a newline and reset current_string
            print()
            current_string = ""
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